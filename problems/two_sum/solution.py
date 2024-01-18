class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()
        for idx in range(len(nums)):
            if nums[idx] in cache:
                return [cache[nums[idx]], idx]
            cache[target-nums[idx]] = idx
            
        