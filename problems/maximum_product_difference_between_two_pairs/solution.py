class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min_ = min__ = float('inf')
        max_ = max__ = float('-inf')
        for num in nums:
            if num <= min_:
                min_, min__, = num, min_
            elif num < min__:
                min__ = num
            if num >= max_:
                max_, max__ = num, max_
            elif num > max__:
                max__ = num
        return max_*max__-min_*min__
        
"""
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]*nums[-2]) - (nums[0]*nums[1])
"""