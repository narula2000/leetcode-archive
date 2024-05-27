class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)+1):
            count = 0
            for j in range(len(nums)):
                if nums[j] >= i:
                    count += 1
            if count == i: return count
        return -1
