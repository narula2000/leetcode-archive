class Solution:
    def areaOfMaxDiagonal(self, dim: List[List[int]]) -> int:
        max_val = max(dim, key=self.dag)
        lst = []
        for val in dim:
            if self.dag(max_val) == self.dag(val):
                lst.append(val)
        
        ans = max(lst, key=self.area)
        return self.area(ans)
    
    def area(self, nums):
        return nums[0] * nums[1]
    
    def dag(self, nums):
        return math.sqrt(nums[0]**2 + nums[1]**2)
        