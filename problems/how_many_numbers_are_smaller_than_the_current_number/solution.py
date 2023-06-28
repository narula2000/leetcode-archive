class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hash = {}
        result = []
        copy = sorted(nums)

        for i, num in enumerate(copy):
            if num not in hash:
                hash[num] = i
        
        return [hash[num] for num in nums]
