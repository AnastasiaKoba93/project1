import unittest


def mult(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def subtract(a, b):
    return a - b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Square root of a negative number is not allowed.")
    return a ** 0.5


class TestMathFunctions(unittest.TestCase):

    def test_mult_positive_numbers(self):
        self.assertEqual(mult(2, 3), 6)

    def test_mult_positive_and_negative_numbers(self):
        self.assertEqual(mult(5, -4), -20)

    def test_mult_negative_numbers(self):
        self.assertEqual(mult(-2, -3), 6)

    def test_mult_by_zero(self):
        self.assertEqual(mult(8, 0), 0)

    def test_division_positive_numbers(self):
        self.assertEqual(division(10, 2), 5)

    def test_division_positive_and_negative_numbers(self):
        self.assertEqual(division(16, -4), -4)

    def test_division_negative_numbers(self):
        self.assertEqual(division(-8, -2), 4)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            division(7, 0)

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 3), 7)

    def test_subtract_positive_and_negative_numbers(self):
        self.assertEqual(subtract(-4, 8), -12)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-6, -3), -3)

    def test_subtract_from_itself(self):
        self.assertEqual(subtract(7, 7), 0)

    def test_power_positive_numbers(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_negative_numbers(self):
        self.assertEqual(power(-2, 4), 16)

    def test_power_to_zero(self):
        self.assertEqual(power(5, 0), 1)

    def test_power_to_one(self):
        self.assertEqual(power(6, 1), 6)

    def test_square_root_positive_number(self):
        self.assertEqual(square_root(25), 5)

    def test_square_root_of_zero(self):
        self.assertEqual(square_root(0), 0)

    def test_square_root_of_negative_number(self):
        with self.assertRaises(ValueError):
            square_root(-9)

    def test_square_root_of_float_number(self):
        self.assertAlmostEqual(square_root(16.5), 4.062, places=4)


if __name__ == '__main__':
    unittest.main()
