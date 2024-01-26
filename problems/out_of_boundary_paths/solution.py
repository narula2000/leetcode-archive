class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}

        @lru_cache(None)
        def recurse(row, col, moves):
            cache = (row, col, moves)
            if not (0 <= row < m and 0 <= col < n): # Out of Bound
                return 1
            elif not moves:
                return 0
            elif cache in memo:
                return memo[cache]
            else:
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                memo[cache] = sum(recurse(row + s_row, col + s_col, moves - 1) for s_row, s_col in directions)
                return memo[cache]
        return recurse(startRow, startColumn, maxMove) % (10**9 + 7)