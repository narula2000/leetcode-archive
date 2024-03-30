class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        memo = defaultdict(int)
        ans, left, right, curr = 0, 0, 0, 0

        while right < len(nums):
            memo[nums[right]] += 1
            if memo[nums[right]] == 1:
                k -= 1
            if k < 0:
                memo[nums[left]] -= 1
                if memo[nums[left]] == 0:
                    k += 1
                left += 1
                curr = 0
            if k == 0:
                while memo[nums[left]] > 1:
                    memo[nums[left]] -= 1
                    left += 1
                    curr += 1
                ans += (curr + 1)
            right += 1
        return ans
