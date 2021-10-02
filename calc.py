import re


class Calc():

    def __init__(self) -> None:
        pass

    def Add(self, numbers: str) -> int:

        if numbers == "":
            return 0
        else:
            nums = re.split('\n|,', numbers)
            sum = 0
            for n in nums:
                sum = sum + int(n)
            return sum
