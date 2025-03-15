import unittest
from calculate import Calculator

class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2,2))
    
    def test_add_method_raises_typeerror(self):
        self.assertRaises(TypeError,self.calc.add, {1}, 2) 

    def test_subtract_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.subtract(4,2))

    def test_subtract_method_raises_typeerror(self):
        self.assertRaises(TypeError, self.calc.subtract, {1}, 2)

    def test_multiply_method_returns_correct_result(self):  
        self.assertEqual(6, self.calc.multiply(2,3))

    def test_multiply_method_raises_typeerror(self):
        self.assertRaises(TypeError, self.calc.multiply, {1}, 2)

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.divide(6,3))

    def test_divide_method_raises_typeerror(self):
        self.assertRaises(TypeError, self.calc.divide, {1}, 2)

    def test_divide_method_raises_valueerror(self):
        self.assertRaises(ValueError, self.calc.divide, 2, 0)

if __name__=='__main__':
    unittest.main()