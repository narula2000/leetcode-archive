class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for row in range(m):
            if grid[row][0] == 0:
                for col in range(n):
                    grid[row][col] = 1 - grid[row][col]
        
        for col in range(1, n):
            num_bit_ones = 0
            for row in range(m):
                if grid[row][col] == 1:
                    num_bit_ones += 1
            if num_bit_ones < m - num_bit_ones:
                for row in range(m):
                    grid[row][col] = 1 - grid[row][col]
        
        score = 0
        for col in range(n):
            num_bit_ones = 0
            for row in range(m):
                if grid[row][col] == 1:
                    num_bit_ones += 1
            
            score += num_bit_ones * 2 ** (n-1 - col)

        return score  
