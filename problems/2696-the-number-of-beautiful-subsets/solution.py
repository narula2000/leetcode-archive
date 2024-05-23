class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        memo = dict()
        def helper(idx):
            if idx == len(nums): return 1
            result = helper(idx+1)
            if not nums[idx] -k in memo and not nums[idx] + k in memo:
                memo[nums[idx]] = memo.get(nums[idx], 0) + 1
                result += helper(idx+1)
                memo[nums[idx]] -= 1
                if memo[nums[idx]] == 0:
                    del memo[nums[idx]]
            return result
        return helper(0) - 1

