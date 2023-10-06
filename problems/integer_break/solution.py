class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            ans = 1
            while n > 4:
                ans, n = ans * 3, n - 3
            return ans * n