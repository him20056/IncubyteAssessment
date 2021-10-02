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

if __name__ == '__main__':
    unittest.main()