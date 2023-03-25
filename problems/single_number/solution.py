class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = dict()
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        for key, val in hash.items():
            if val == 1:
                return key
        return -1