import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        #Initialize the calculator object before each test.
        self.calculator = SimpleCalculator()

    def test_add(self):
        #Test addition method.
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        #Test subtraction method.
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        #Test multiplication method.
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 10), 0)

    def test_divide(self):
        #Test division method, including division by zero.
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(0, 3), 0)
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0), "Expected None when dividing by zero")

if __name__ == "__main__":
    unittest.main()

