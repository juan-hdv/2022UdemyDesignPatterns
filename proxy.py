"""
Proxy Coding Exercise
You are given the Person  class and asked to write a ResponsiblePerson  proxy that does the following:

Allows person to drink unless they are younger than 18 (in that case, return "too young")

Allows person to drive unless they are younger than 16 (otherwise, "too young")

In case of driving while drink, returns "dead", regardless of age
"""

from unittest import TestCase


class Person:
  def __init__(self, age):
    self.age = age

  def drink(self):
    return 'drinking'

  def drive(self):
    return 'driving'

  def drink_and_drive(self):
    return 'driving while drunk'

class ResponsiblePerson:
  def __init__(self, person):
    self.person = person

  @property
  def age(self):
    return self.person.age

  @age.setter
  def age(self, years):
    self.person.age = years

  def drink(self):
    return "too young" if self.person.age < 18 else self.person.drink()

  def drive(self):
    return "too young" if self.person.age < 16 else self.person.drive()

  def drink_and_drive(self):
    return 'dead'

class Evaluate(TestCase):
  def test_exercise(self):
    p = Person(10)
    rp = ResponsiblePerson(p)

    self.assertEqual('too young', rp.drive())
    self.assertEqual('too young', rp.drink())
    self.assertEqual('dead', rp.drink_and_drive())

    rp.age = 20

    self.assertEqual('driving', rp.drive())
    self.assertEqual('drinking', rp.drink())
    self.assertEqual('dead', rp.drink_and_drive())

p = Person(12)
rp = ResponsiblePerson(p)
print(rp.drive())
print(rp.drink())
print(rp.drink_and_drive())

print ("------")

rp.age = 20
print(rp.drive())
print(rp.drink())
print(rp.drink_and_drive())

