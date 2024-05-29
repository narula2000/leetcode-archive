class Solution:
    def numSteps(self, s: str) -> int:
        val, ans = int(s, 2), 0
        while val > 1:
            if val % 2 == 0: val //= 2
            else: val += 1
            ans += 1
        return ans
