"""
Strategy Coding Exercise
Consider the quadratic equation and its canonical solution:

The part b^2-4*a*c is called the discriminant. 
Suppose we want to provide an API with two different strategies for calculating the discriminant:

In OrdinaryDiscriminantStrategy , If the discriminant is negative, we return it as-is. 
This is OK, since our main API returns Complex  numbers anyway.

In RealDiscriminantStrategy , if the discriminant is negative, the return value is NaN (not a number). 
NaN propagates throughout the calculation, so the equation solver gives two NaN values. 
In Python, you make such a number with float('nan').

Please implement both of these strategies as well as the equation solver itself. 
With regards to plus-minus in the formula, please return the + result as the first element and - as the second. 
Note that the solve() method is expected to return complex values.
"""
from abc import ABC
import math
from unittest import TestCase


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        self.discriminant = b**2 - 4*a*c


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        super().calculate_discriminant(a, b, c)


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        super().calculate_discriminant(a, b, c)
        if self.discriminant < 0:
            self.discriminant = float('nan')


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        self.strategy.calculate_discriminant(a, b, c)
        discriminant = self.strategy.discriminant

        if math.isnan(discriminant):
            result1 = complex(float('nan'), float('nan'))
            result2 = complex(float('nan'), float('nan'))
        elif discriminant < 0:
            real = -b/(2*a)
            imaginary = abs(discriminant)**0.5/2*a
            result1 = complex(real, imaginary)
            result2 = complex(real, -imaginary)
        else:
            real = -b/(2*a)
            result1 = complex(real + (discriminant**0.5)/2*a, 0)
            result2 = complex(real - (discriminant**0.5)/2*a, 0)

        return (result1, result2)


class Evaluate(TestCase):
    def test_positive_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), results[0])
        self.assertEqual(complex(-8, 0), results[1])

    def test_positive_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), results[0])
        self.assertEqual(complex(-8, 0), results[1])

    def test_negative_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 4, 5)
        self.assertEqual(complex(-2, 1), results[0])
        self.assertEqual(complex(-2, -1), results[1])

    def test_negative_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 4, 5)
        self.assertTrue(math.isnan(results[0].real))
        self.assertTrue(math.isnan(results[1].real))
        self.assertTrue(math.isnan(results[0].imag))
        self.assertTrue(math.isnan(results[1].imag))
