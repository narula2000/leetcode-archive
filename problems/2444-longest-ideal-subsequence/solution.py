class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        memo = [0] * 128
        for char in s:
            val = ord(char)
            memo[val] = max(memo[val-k:val+k+1]) + 1
        return max(memo)
