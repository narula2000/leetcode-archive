class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        stack = sorted(nums)
        current = sum(stack)
        while stack and current <= stack[-1] * 2:
            current -= stack.pop()
        return sum(stack) if len(stack) > 2 else -1
        