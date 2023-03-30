class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = dict()
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        for key, val in hash.items():
            if val > len(nums) / 2:
                return key

"""
class EditorialSolution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
"""