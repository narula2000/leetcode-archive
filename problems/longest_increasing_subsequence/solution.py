class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        memo = [1] * N

        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N): # From i onwards
                if nums[i] < nums[j]:
                    memo[i] = max(memo[i], 1 + memo[j])
            
        return max(memo)