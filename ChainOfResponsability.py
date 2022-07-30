"""
Chain of Responsibility Coding Exercise

You are given a game scenario with classes Goblin and GoblinKing.

Please implement the following rules:

* A goblin has base 1 attack / 1 defense (1/1), a goblin king is 3/3.

* When the Goblin King is in play, every other goblin gets +1 Attack.

* Goblins get +1 to Defense for every other Goblin in play
(a GoblinKing is a Goblin!).

Example:

Suppose you have 3 ordinary goblins in play. Each one is a 1/3
(1/1 + 0/2 defense bonus).

A goblin king comes into play. Now every goblin is a 2/4
(1/1 + 0/3 defense bonus from each other + 1/0 from goblin king)

The state of all the goblins has to be consistent as goblins are
added and removed from the game.

Here is an example of the kind of test that will be run on the system:

class FirstTestSuite(unittest.TestCase):
    def test(self):
        game = Game()
        goblin = Goblin(game)
        game.creatures.append(goblin)

        self.assertEqual(1, goblin.attack)
        self.assertEqual(1, goblin.defense)
Note: creature removal (unsubscription) does not need to be implemented.
"""


from abc import ABC
from enum import Enum
import unittest

from pytest import skip


class Creature(ABC):
    def __init__(self, game, attack, defense):
        self.initial_defense = defense
        self.initial_attack = attack
        self.game = game
        self.game.creatures.append(self)

    @property
    def attack(self): pass

    @property
    def defense(self): pass

    def change_attribute(self, source, attribute): pass


class Attribute(Enum):
    ATTACK = 1
    DEFENSE = 2

class Goblin (Creature):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack, defense)

    @property
    def attack(self):
        q = AttributeChange(Attribute.ATTACK, self.initial_attack)
        for c in self.game.creatures:
            c.change_attribute(self, q)
        return q.value

    @property
    def defense(self):
        q = AttributeChange(Attribute.DEFENSE, self.initial_defense )
        for c in self.game.creatures:
            c.change_attribute(self, q)
        return q.value

    def change_attribute(self, source, attribute):
        if self != source and attribute.name == Attribute.DEFENSE:
            attribute.value += 1

    def __str__(self) -> str:
        return f"Goblin attack {self.attack} / defense {self.defense}"

class GoblinKing(Goblin):
    def __init__(self, game):
        super().__init__(game, 3, 3)

    def change_attribute(self, source, attribute):
        if self != source and attribute.name == Attribute.ATTACK:
            attribute.value += 1
        else:
            super().change_attribute(source, attribute)

    def __str__(self) -> str:
        return "KING " + super().__str__()

class AttributeChange:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Game:
    def __init__(self):
        self.creatures = []

    def __str__(self) -> str:
        return "\n".join([str(g) for g in self.creatures])


class FirstTestSuite(unittest.TestCase):

    def test1(self):
        game = Game()
        goblin = Goblin(game)

        self.assertEqual(1, goblin.attack)
        self.assertEqual(1, goblin.defense)

        goblin2 = Goblin(game)

        self.assertEqual(1, goblin.attack)
        self.assertEqual(2, goblin.defense)

        goblin3 = GoblinKing(game)

        self.assertEqual(2, goblin.attack)
        self.assertEqual(3, goblin.defense)

    #@unittest.skip(reason="")
    def test2(self):
        game = Game()
        goblin = Goblin(game)

        self.assertEqual(1, goblin.attack)
        self.assertEqual(1, goblin.defense)

        game2 = Game()
        g1 = Goblin(game2)
        g2 = Goblin(game2)
        g3 = Goblin(game2)

        # Suppose you have 3 ordinary goblins in play. Each one is a 1/3
        self.assertEqual(1, g1.attack)
        self.assertEqual(3, g1.defense)
        self.assertEqual(1, g2.attack)
        self.assertEqual(3, g2.defense)
        self.assertEqual(1, g3.attack)
        self.assertEqual(3, g3.defense)

        # A goblin king comes into play. Now every goblin is a 2/4
        k1 = GoblinKing(game2)

        self.assertEqual(3, k1.attack)
        self.assertEqual(6, k1.defense)
        self.assertEqual(2, g1.attack)
        self.assertEqual(4, g1.defense)
        self.assertEqual(2, g2.attack)
        self.assertEqual(4, g2.defense)
        self.assertEqual(2, g3.attack)
        self.assertEqual(4, g3.defense)


game = Game()
goblin = Goblin(game)

print(game)
print("--------")

game2 = Game()
g1 = Goblin(game2)
g2 = Goblin(game2)
g3 = Goblin(game2)

# Suppose you have 3 ordinary goblins in play. Each one is a 1/3
print(game2)
print("--------")

# A goblin king comes into play. Now every goblin is a 2/4
k1 = GoblinKing(game2)

print(game2)
print("--------")
