class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        mapping = {}
        ans = 0
        start_idx = 0
        for i in range(n):
            start_idx = max(start_idx, mapping.get(nums[i], -1) + 1)
            ans = max(ans, prefixSum[i + 1] - prefixSum[start_idx])
            mapping[nums[i]] = i

        return ans

        