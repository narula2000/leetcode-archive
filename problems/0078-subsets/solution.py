class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, start, ops, res):
            if start == len(nums):
                res.append(ops.copy())
                return
            helper(nums, start+1, ops, res)
            ops.append(nums[start])
            helper(nums, start+1, ops, res)
            ops.pop()
        ans = []
        helper(nums, 0, [], ans)
        return ans
