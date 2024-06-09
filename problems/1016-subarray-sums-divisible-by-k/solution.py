class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        memo = {0: 1}
        prefix, ans = 0, 0
        for num in nums:
            prefix += num
            left = prefix % k
            if left < 0:
                left += k
            if left in memo:
                ans += memo[left]
                memo[left] += 1
            else:
                memo[left] = 1
        return ans
            

