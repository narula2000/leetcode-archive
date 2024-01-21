class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if not nums:
            return 0
        
        s0, s1 = [0, 0], [0, 0]
        s1[0] = nums[0]

        for i in range(1, N):
            s0[i % 2] = max(s0[(i - 1) % 2], s1[(i - 1) % 2])
            s1[i % 2] = s0[(i - 1) % 2] + nums[i]
        
        return max(s0[(N - 1) % 2], s1[(N - 1) % 2])
