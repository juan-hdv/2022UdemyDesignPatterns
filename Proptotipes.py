"""
Given the definitions shown in code, you are asked to implement line.deep_copy() 
to perform a deep copy of the given line object.

This method should return a copy of the line that contanis copies of its starts/end points
Please don't confuse deep_copy() with __deepcopy__()
"""
import copy

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        return copy.deepcopy(self)


        