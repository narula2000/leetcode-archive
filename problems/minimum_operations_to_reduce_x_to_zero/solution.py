class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target, N = sum(nums) - x, len(nums)

        if target == 0:
            return N

        curr = max_len = left = 0

        for right in range(len(nums)):
            curr += nums[right]
            while left <= right and curr > target:
                curr -= nums[left]
                left += 1
            if curr == target:
                max_len = max(max_len, right - left + 1)
            
        return N - max_len if max_len else -1