class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for c,i in enumerate(nums):
            if c<len(nums):
                for v,j in enumerate(nums[c+1:]):
                    if i + j == target:
                        return [c,c+v+1]
                    