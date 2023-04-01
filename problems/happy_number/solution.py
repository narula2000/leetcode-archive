class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 2 or n == 3 or n == 4:
            return False
        else:
            nums = str(n)
            result = 0
            for char in nums:
                result += int(char)**2
            return self.isHappy(result)
        