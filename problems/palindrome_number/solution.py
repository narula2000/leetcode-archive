class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringInt = str(x)
        n = len(stringInt)
        for i in range(n):
            if (stringInt[i] != stringInt[(n - 1) - i]):
                return False
        return True