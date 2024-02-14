class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [num for num in nums if num > -1]
        neg = [num for num in nums if num < 0]
        return [i for pair in zip(pos, neg) for i in pair]
