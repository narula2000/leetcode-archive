class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        if M < N:
            t1, t2 = text2, text1
        
        memo = [0] * (N+1)

        for char in text1:
            prev_row, prev_col = 0, 0
            for j in range(len(text2)):
                prev_row, prev_col = memo[j + 1], prev_row
                memo[j + 1] = prev_col + 1 if char == text2[j] else max(memo[j], prev_row)
        return memo[-1]

        