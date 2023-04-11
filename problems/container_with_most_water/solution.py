class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, area = 0, len(height) -1, float('-inf')
        while left < right:
            gap = right - left
            max_computable_height = min(height[left], height[right])
            area = max(area, max_computable_height * gap)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return area

