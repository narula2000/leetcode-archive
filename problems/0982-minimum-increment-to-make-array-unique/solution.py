class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        track, ans = 0, 0
        for num in nums:
            track = max(track, num)
            ans += track - num
            track += 1
        return ans
