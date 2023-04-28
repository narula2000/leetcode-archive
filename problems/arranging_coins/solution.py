class Solution:
    def arrangeCoins(self, n: int) -> int:
        result, idx = 0, 0
        while True:
            idx += 1
            n -= idx
            result += 1

            if n <= idx:
                return result
