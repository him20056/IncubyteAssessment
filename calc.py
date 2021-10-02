import re


class Calc():

    def __init__(self) -> None:
        pass

    def Add(self, numbers: str) -> int:

        if numbers == "":
            return 0
        else:
            nums = self.GetNumbers(numbers)
            sum = 0
            negative = []
            for n in nums:
                if int(n) < 0:
                    negative.append(n)
                elif negative == []:
                    sum = sum + int(n)
            if negative != []:
                raise Exception("negatives not allowed " + ','.join(negative))
            else:
                return sum
    
    def GetNumbers(self, nums: str):
        if nums.startswith('//'):
            new_del = re.split('//|\n', nums)[1]
            delimiter = '\n|' + new_del
            return re.split(delimiter, nums)[2:]
        else:
            delimiter = '\n|,'
            return re.split(delimiter, nums)
