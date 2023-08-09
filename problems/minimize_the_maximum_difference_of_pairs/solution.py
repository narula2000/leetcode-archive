class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def is_possible(nums, p, diff):
            n = len(nums)
            i = 1
            while i < n:
                if nums[i] - nums[i - 1] <= diff:
                    p -= 1
                    i += 1 # Shift to other pairs
                i += 1

            return p <= 0
        
        nums.sort()
        left, right = 0, nums[-1] - nums[0] # Right is the largest diff
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if is_possible(nums, p, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans