class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            middle = (low + high) // 2
            val = nums[middle]
            if val == target:
                return middle
            if target < val:
                high = middle - 1
            else:
                low = middle + 1
        return low