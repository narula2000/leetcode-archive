class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return sum(v for k, v in counter.items() if v == max(counter.values()))