class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        ans = []
        for key, val in count.items():
            if val > 1:
                ans.append(key)
        
        for i in range(1, len(nums)+1):
            if i not in count.keys():
                ans.append(i)
        
        return ans
