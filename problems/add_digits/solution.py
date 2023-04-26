class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            nums = [int(char) for char in str(num)]
            num = sum(nums)
        return num