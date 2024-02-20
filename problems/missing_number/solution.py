class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        _nums = set(nums)
        for i in range(len(nums)+1):
            if i not in _nums:
                return i
        return -1
