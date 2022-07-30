"""
A magic square is a square matrix of numbers where the sum in each row,
each column, and each of the diagonals is the same.

You are given a system of 3 classes that can be used to make a magic square.
The classes are:

Generator: this class generates a 1-dimensional list of random digits
in range 1 to 9.

Splitter: this class takes a 2D list and splits it into all possible
arrangements of 1D lists.
It gives you the columns, the rows and the two diagonals.

Verifier: this class takes a 2D list and verifies that the sum of elements
in every sublist is the same.

Please implement a Façade class called MagicSquareGenerator  which simply
generates the magic square of a given size.
"""

from random import randint
from unittest import TestCase


class Generator:
    def generate(self, count):
        return [randint(1, 9) for x in range(count)]


class Splitter:
  def split(self, array):
    result = []

    row_count = len(array)
    col_count = len(array[0])

    for r in range(row_count):
      the_row = []
      for c in range(col_count):
        the_row.append(array[r][c])
      result.append(the_row)

    for c in range(col_count):
      the_col = []
      for r in range(row_count):
        the_col.append(array[r][c])
      result.append(the_col)

    diag1 = []
    diag2 = []

    for c in range(col_count):
      for r in range(row_count):
        if c == r:
          diag1.append(array[r][c])
        r2 = row_count - r - 1
        if c == r2:
          diag2.append(array[r][c])

    result.append(diag1)
    result.append(diag2)

    return result


class Verifier:
    def verify(self, arrays):
        if not arrays:
            return False
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:

    def generate(self, size) ->list:
        # todo - return a magic square of the given size
        
        gen = Generator()
        spl = Splitter()
        ver = Verifier()

        magic = False
        tries = float("inf")
        while not magic and tries > 0:
            array_2d = [gen.generate(size) for _ in range(size)]
            if ver.verify(spl.split(array_2d)):
                magic = True

            # print(f"{tries}", "+" if magic else "- ",array)
            # print(" >>",array_splited)
            tries -=1

        return array_2d if magic else []

class Evaluate(TestCase):
  def test_exercise(self):
    gen = MagicSquareGenerator()
    square = gen.generate(3)

    print("Result: ", square)

    v = Verifier()
    self.assertTrue(v.verify(square),
                    'Verification failed. '
                    'This is not a valid magic square.')
