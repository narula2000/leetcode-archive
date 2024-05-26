class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7
        memo = [[[-1]*3 for _ in range(2)] for _ in range(n+1)]
        def helper(idx, _abs, late):
            if _abs >= 2 or late >= 3: return 0
            if idx == 0: return 1
            if memo[idx][_abs][late] != -1: return memo[idx][_abs][late]
            ans = helper(idx-1, _abs, 0)
            ans += helper(idx-1, _abs, late+1)
            ans += helper(idx-1, _abs+1, 0)
            memo[idx][_abs][late] = ans % mod
            return memo[idx][_abs][late]
        return helper(n, 0, 0)
