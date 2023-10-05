class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return [key for key, val in count.items() if val > len(nums)/3]