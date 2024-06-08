class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sums, prev, seen = 0, 0, set()
        for num in nums:
            sums += num
            if sums % k in seen: return True
            seen.add(prev)
            prev = sums % k
        return False
