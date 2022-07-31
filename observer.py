"""Observer Coding Exercise
Imagine a game where one or more rats can attack a player.
Each individual rat has an initial attack value of 1.
However, rats attack as a swarm, so each rat's attack value is actually equal to the total number of rats in play.
Given that a rat enters play through the initializer and leaves play (dies) via its __exit__ method, 
please implement the Game and Rat classes so that, at any point in the game, the Attack value of a rat is always consistent.
"""
from unittest import TestCase


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self):
        self.player_add = Event()
        self.player_remove = Event()
        self.player_notify = Event()


class Rat:
    count = 0

    @classmethod
    def add_count(cls):
        cls.count += 1
        return cls.count

    def __init__(self, game):
        self.name = f"Rat {Rat.add_count()}"
        self.game = game
        self.attack = 1

        game.player_add.append(self.rat_enters)
        game.player_notify.append(self.notify_rat)
        game.player_remove.append(self.rat_dies)

        self.game.player_add(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.player_remove(self)

    def rat_enters(self, rat):
        if rat != self:
            print(f"rat_enters::{self.name} / {rat.name}")
            self.attack += 1
            self.game.player_notify(rat)

    def notify_rat(self, rat):
        if rat == self:
            print(f"notify_rat::{self.name} / {rat.name}")
            self.attack += 1

    def rat_dies(self, rat):
        print(f"rat_dies::{self.name} / {rat.name}")
        self.attack -= 1


class Evaluate(TestCase):
    def test_single_rat(self):
        game = Game()
        rat = Rat(game)
        self.assertEqual(1, rat.attack)

    def test_two_rats(self):
        game = Game()
        rat = Rat(game)
        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

    def test_three_rats_one_dies(self):
        game = Game()

        rat = Rat(game)
        self.assertEqual(1, rat.attack)

        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

        with Rat(game) as rat3:
            self.assertEqual(3, rat.attack)
            self.assertEqual(3, rat2.attack)
            self.assertEqual(3, rat3.attack)

        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

        self.fail()

g = Game()
for k in range(5):
    print("Start")
    r = Rat(g)
    print(f"End {r.name}")
    print("-----\n")
