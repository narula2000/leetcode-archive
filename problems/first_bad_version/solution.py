# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid): # go lower
                right = mid
            else: # go higher
                left = mid + 1
        
        return left

