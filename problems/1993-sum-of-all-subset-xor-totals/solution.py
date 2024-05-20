class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def helper(nums, lvl, curr):
            if lvl == len(nums): return curr
            return helper(nums, lvl+1, curr^nums[lvl]) + helper(nums, lvl+1, curr)
        return helper(nums, 0, 0)

