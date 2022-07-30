from typing import Any
import unittest


class EventsFactory(list):
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        for item in self:
            item(*args, **kwargs)


class Participant:
    def __init__(self, mediator, name=""):
        self.value = 0
        self.name = name
        self.mediator = mediator
        self.mediator.events.append(self.trigger_value_change)

    def say(self, value):
        self.mediator.broadcast(self, value)

    # Events triggered when broadcasting
    def trigger_value_change(self, sender, value):
        if self != sender:
            self.value += value


class Mediator:
    def __init__(self) -> None:
        self.events = EventsFactory()

    def broadcast(self, sender, value):
        self.events(sender, value)


class FirstTestSuite(unittest.TestCase):
    def test(self):
        m = Mediator()
        p1 = Participant(m)
        p2 = Participant(m)

        self.assertEqual(0, p1.value)
        self.assertEqual(0, p2.value)

        p1.say(2)

        self.assertEqual(0, p1.value)
        self.assertEqual(2, p2.value)

        p2.say(4)

        self.assertEqual(4, p1.value)
        self.assertEqual(2, p2.value)
        
# -------


def print_participants():
    print(f"Participants:")
    print(f"{p1.name} : {p1.value}")
    print(f"{p2.name} : {p2.value}")
    print("---")


med = Mediator()
p1 = Participant(med, "p1")
p2 = Participant(med, "p2")
print_participants()

p1.say(2)
print_participants()

p2.say(4)
print_participants()
