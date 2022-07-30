# MEDIATOR USING THE EVENT PATTERN
import unittest


class EventFactory(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        mediator.alert.append(self.mediator_alert)

    def say(self, value):
        self.mediator.broadcast(self, value)

    def mediator_alert(self, sender, value):
        if sender != self:
            self.value += value


class Mediator:
    def __init__(self):
        self.alert = EventFactory()

    def broadcast(self, sender, value):
        self.alert(sender, value)


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
