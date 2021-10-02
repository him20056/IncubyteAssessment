import unittest
from calc import Calc

class TestCalc(unittest.TestCase):
    def __init__(self, methodName: str = None) -> None:
        super().__init__(methodName=methodName)
        self.calc = Calc()

    def test_Add_blankString(self):
        self.assertEqual(self.calc.Add(""), 0, "If no string provided, answer should be 0")
    

if __name__ == '__main__':
    unittest.main()