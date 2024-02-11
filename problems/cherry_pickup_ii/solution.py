class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        memo_prev = defaultdict(lambda: -float("inf"))
        memo_prev[(0, n - 1)] = grid[0][0] + grid[0][n - 1]
        for row in grid[1:]:
            memo = defaultdict(lambda: -float("inf"))
            for i in range(n):
                for j in range(i, n):
                    memo[(i, j)] = (
                        row[i] + row[j] if i != j else row[i]
                    ) + max(
                        memo_prev[(i + d_i, j + d_j)]
                        for d_i in {-1, 0, 1}
                        for d_j in {-1, 0, 1}
                    )
            memo_prev = memo
        return max(memo.values())