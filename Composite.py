"""
Composite Coding Exercise

We have two classes called SingleValue and ManyValues. 
SingleValue stores just one numeric value
ManyValues can store either numeric values or SingleValue objects.

You are asked to give both SingleValue and ManyValues a property member called sum that returns a sum of all the values that the object contains. 
Please ensure that there is only a single method that realizes the property sum, not multiple methods.

Here is a sample unit test:

single_value=SingleValue(11)
other_values=ManyValues()
other_values.append(22)
other_values.append(33)
# make a list of all values
all_values = ManyValues()
all_values.append (single_value)
all_values.append (other_values)
self. assertEqual(all_values.sum, 66)
"""

from abc import ABC
from typing import Iterable
from unittest import TestCase

class Sumable (Iterable, ABC):
    @property
    def sum(self):
        # This sum will sum several levels of objects, not only 2 levels
        result = 0
        for e in self:
            result += e if type(e) == int else e.sum

        return result

class SingleValue (Sumable):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value
    
    def __len__(self) -> int:
        return 1
        
class ManyValues(list, Sumable):
    ...

class TestComposite (TestCase):
    def test_sum(self):
        single_value=SingleValue(22)

        other_values=ManyValues()
        other_values.append(33)
        other_values.append(44)

        # make a list of all values
        all_values = ManyValues()
        all_values.append (single_value)
        all_values.append (other_values)

        third_level_values = ManyValues()
        third_level_values.append(single_value)
        third_level_values.append(other_values)
        third_level_values.append(all_values)
        third_level_values.append(2)

        self.assertEqual(all_values.sum, 22+33+44)
        self.assertEqual(third_level_values.sum, 22+(33+44)+99+2)
