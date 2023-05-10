class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()

        for idx, val in enumerate(nums):
            diff = target - val
            if val in hash:
                return [hash[val], idx]
            hash[diff] = idx