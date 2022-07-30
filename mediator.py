"""
Mediator Coding Exercise
Our system has any number of instances of Participant classes.
Each Participant has a value integer attribute, initially zero.

A participant can say() a particular value, which is broadcasted 
to all other participants.

At this point in time, every other participant is obliged to increase
their value  by the value being broadcast.

Example:
Two participants start with values 0 and 0 respectively

Participant 1 broadcasts the value 3. We now have:
   Participant 1 value = 0, Participant 2 value = 3
Participant 2 broadcasts the value 2. We now have:
   Participant 1 value = 2, Participant 2 value = 3
"""
import unittest


class Participant:
    def __init__(self, mediator, name=""):
        self.value = 0
        self.name = name
        self.mediator = mediator
        self.mediator.add_participant(self)

    def say(self, value):
        self.mediator.broadcast(self, value)


class Mediator:
    def __init__(self) -> None:
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def broadcast(self, who, value):
        for p in self.participants:
            if p != who:
                p.value = value

    def __str__(self) -> str:
        result = ""
        for p in self.participants:
            result += f"Participant {p.name} with Value: {p.value}\n"
        return result


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


med = Mediator()
p1 = Participant(med, "p1")
p2 = Participant(med, "p2")
print()
print("Participants:")
print(med)
print("---")

p1.say(3)
p2.say(2)
