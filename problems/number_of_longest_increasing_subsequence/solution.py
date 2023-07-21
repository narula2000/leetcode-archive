class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 1
        hash = [1] * N
        count = [1] * N
        max_ = 0

        # Longest Increasing Subsequence == LIS
        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j]: # Check for potential IS
                    if hash[j] + 1 > hash[i]:
                        hash[i] = hash[j] + 1 # Keep the length of IS
                        count[i] = count[j]
                    elif hash[i] == hash[j] + 1:
                        count[i] += count[j]
            
            max_ = max(max_, hash[i])
        
        result = 0
        for i in range(N): # Find all LIS
            if hash[i] == max_:
                result += count[i]
        
        return result