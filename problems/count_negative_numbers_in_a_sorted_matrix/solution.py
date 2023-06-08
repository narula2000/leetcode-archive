class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for row in grid:
            for idx, col_val in enumerate(row):
                if col_val < 0:
                    count += len(row) - idx
                    break
        return count