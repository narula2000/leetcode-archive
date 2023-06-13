class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i].sort()

        transpose = list(zip(*grid))

        return sum(max(row) for row in transpose)

"""
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        result = 0
        for _ in range(len(grid[0])):
            maxx_ = float('-inf')
            for row in grid:
                max_ = max(row)
                row.remove(max_)
    
                maxx_ = max(max_, maxx_)
            result += maxx_
        
        return result
"""