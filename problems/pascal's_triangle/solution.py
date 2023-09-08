class Solution:
    def generate(self, nums: int) -> List[List[int]]:
        res  = [[1]]
        for i in range(1, nums):
            curr = [1]

            j = 1
            while j < i:
                val = prev[j-1] + prev[j]
                curr.append(val)
                j += 1
        
            curr.append(1)
            res.append(curr)

            prev = curr
        
        return res