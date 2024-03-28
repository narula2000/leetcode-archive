class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans, left, memo, N = 0, 0, dict(), len(nums)

        for right in range(N):
            memo[nums[right]] = memo.get(nums[right], 0) + 1
            if memo[nums[right]] > k:
                while nums[left] != nums[right]:
                    memo[nums[left]] -= 1
                    left += 1
                memo[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
