class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums = list(set(nums1).intersection(set(nums2)))
        return -1 if len(nums) < 1 else min(nums)

