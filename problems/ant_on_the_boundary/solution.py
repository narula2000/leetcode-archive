class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        curr = ans = 0
        for step in nums:
            curr += step
            if curr == 0:
                ans += 1
        return ans