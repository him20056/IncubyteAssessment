import unittest
from calc import Calc

class TestCalc(unittest.TestCase):
    def __init__(self, methodName: str = None) -> None:
        super().__init__(methodName=methodName)
        self.calc = Calc()

    def test_Add_blankString(self):
        self.assertEqual(self.calc.Add(""), 0, "If no string provided, answer should be 0")

    def test_Add_single_number(self):
        self.assertEqual(self.calc.Add("5"), 5, "answer should be 5")
    
    def test_Add_Multiple_numbers(self):
        self.assertEqual(self.calc.Add("1,2,3"), 6, "answer should be 6")
    
    def test_Add_Multiple_numbers_with_new_line(self):
        self.assertEqual(self.calc.Add("1,2\n3"), 6, "answer should be 6")

    def test_Add_Custom_Delimeter(self):
        self.assertEqual(self.calc.Add('//;\n1;2;3\n4'), 10, "anser should be 10")

    def test_Add_Raises_ValueError(self):
        # It should raise ValueError as '2,\n3' is stated Invalid in assignment
        self.assertRaises(ValueError, self.calc.Add, '1,2,\n3')
    
    def test_Add_Raises_Exception_Negative_numbers(self):
        # It should raise Exception in case of negative numbers
        self.assertRaises(Exception, self.calc.Add, '-1,2')

if __name__ == '__main__':
    unittest.main()