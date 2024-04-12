class Solution:
    def trap(self, height: List[int]) -> int:
        ans, i, j, = 0, 0, len(height) - 1
        left, right = height[i], height[j]
        while i < j:
            if left < right:
                ans += left - height[i]
                i += 1
                left = max(left, height[i])
            else:
                ans += right - height[j]
                j -= 1
                right = max(right, height[j])
        return ans

