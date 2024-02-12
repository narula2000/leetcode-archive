class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        count = 1
        for i in range(1, len(nums)):
            count += (1 if curr == nums[i] else -1)
            if not count:
                curr = nums[i]
                count = 1
        return curr
