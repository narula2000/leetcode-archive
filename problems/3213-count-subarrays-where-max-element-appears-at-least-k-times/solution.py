class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_ele = max(nums) 
        ans, left, max_window = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] == max_ele:
                max_window += 1
            while max_window == k:
                if nums[left] == max_ele:
                    max_window -= 1
                left += 1
            ans += left
        return ans
