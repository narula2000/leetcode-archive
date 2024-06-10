class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected, ans = sorted(heights), 0
        for i in range(len(heights)):
            if expected[i] != heights[i]: ans += 1
        return ans
