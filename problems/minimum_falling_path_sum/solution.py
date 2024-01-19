class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def helper(i, j):
            if i < 0 or j < 0 or i > N - 1 or j > N - 1: # Out of Bounds
                return float("inf")
            if (i, j) in memo:
                return memo[(i, j)]
            val = grid[i][j]
            if i == N - 1: # Last row
                return val
            
            result = val + min(helper(i+1, j), helper(i+1, j+1), helper(i+1, j-1))
            memo[(i, j)] = result
            return result
        
        grid = matrix
        N = len(grid)
        ans = float("inf")
        memo = dict()
        for i in range(N):
            ans = min(ans, helper(0, i))
        return ans

