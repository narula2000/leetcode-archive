class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        val = nums[0]
        
        if len(nums) == 1:
            return val + 1
        
        idx = -1
        for i in range(1, len(nums)):
            if nums[i] - val != 1:
                idx = i
                break
            val = nums[i]
        
        
        ans = sum(nums[:idx])
        if idx == -1:
            return sum(nums)
        
        while ans in nums:
            ans += 1
        
        return ans