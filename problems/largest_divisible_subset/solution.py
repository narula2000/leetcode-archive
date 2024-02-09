class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        memo = [[]]
        for num in sorted(nums):
            tmp = []
            for mem in memo:
                if not mem or num % mem[-1] == 0:
                    tmp.append(mem + [num])
            memo.append(max(tmp, key=len))
        
        return max(memo, key=len)