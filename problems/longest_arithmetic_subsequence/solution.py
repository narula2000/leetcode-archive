class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        hash = {}
        for i in range(1, len(nums)):
            for j, num in enumerate(nums[:i]):
                diff = nums[i] - num

                if (j, diff) in hash:
                    hash[i, diff] = hash[j, diff] + 1
                else:
                    hash[i, diff] = 2
        
        return max(hash.values())