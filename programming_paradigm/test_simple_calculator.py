import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)

    def test_subtraction(self):
        """Test subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-2, -2), 0)
        self.assertEqual(self.calc.subtract(-5, 3), -8)

    def test_multiplication(self):
        """Test multiply method."""
        self.assertEqual(self.calc.multiplication(2, 3), 6)
        self.assertEqual(self.calc.multiplication(0, 100), 0)
        self.assertEqual(self.calc.multiplication(-2, 3), -6)
        self.assertEqual(self.calc.multiplication(-4, -5), 20)

    def test_division(self):
        """Test divide method, including division by zero."""
        self.assertEqual(self.calc.division(10, 2), 5)
        self.assertEqual(self.calc.division(-9, 3), -3)
        self.assertEqual(self.calc.division(5, 2), 2.5)
        self.assertIsNone(self.calc.division(5, 0))  # division by zero

if __name__ == "__main__":
    unittest.main()
