class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrace(ans, visited, subset, nums):
            if len(subset) == len(nums):
                ans.append(subset)
            
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    backtrace(ans, visited, subset+[nums[i]], nums)
                    visited.remove(i)

        result = [] 
        backtrace(result, set(), [], nums)
        return result
