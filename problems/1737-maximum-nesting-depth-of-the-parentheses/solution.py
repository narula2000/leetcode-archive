class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth, count = 0, 0
        for char in s:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
            max_depth = max(max_depth, count)
        return max_depth
