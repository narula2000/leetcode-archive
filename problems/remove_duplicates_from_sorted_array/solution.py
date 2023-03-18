class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check_val = None
        change_idx = 0
        idx = 0
        while idx < len(nums):
            if nums[idx] != check_val:
                check_val, nums[change_idx] = nums[idx], nums[idx]
                change_idx += 1
            idx += 1
        for _ in range(len(nums) - change_idx):
            nums.pop()
        return change_idx + 1