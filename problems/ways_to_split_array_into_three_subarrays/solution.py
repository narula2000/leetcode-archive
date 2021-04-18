from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)

        ans = 0
        for i in range(1, len(nums)):
            left = bisect_left(prefixSum, 2 * prefixSum[i])
            right = bisect_right(
                prefixSum, (prefixSum[i] + prefixSum[-1]) // 2)
            ans += max(0, min(len(nums), right) - max(i + 1, left))

        return ans % (10**9 + 7)
        