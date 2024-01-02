class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        ans = []

        for num in nums:
            row = count[num]

            if len(ans) == row: # Found duplicate
                ans.append([])
            
            ans[row].append(num)
            count[num] += 1
            
        return ans