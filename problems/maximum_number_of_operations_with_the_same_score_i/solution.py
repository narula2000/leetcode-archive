class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        score = idx = ans = 0
        
        while idx <= len(nums)-2:
            val = nums[idx:idx+2]
            print(val, sum(val))
            
            if idx == 0:
                score = sum(val)
            
            if score != sum(val):
                return ans
            ans += 1
            idx += 2
        
        return ans