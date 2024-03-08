class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        arr = [(freq, key) for key, freq in count.items()]
        return sum(freq for key, freq in count.items() if freq == max(arr)[0])

