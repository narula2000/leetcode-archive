class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        memo = [[False]*N for _ in range(N)]
        ans = 0
        for i in range(N):
            memo[i][i] = True
            ans += 1
        
        for i in range(N-1):
            if s[i] == s[i+1]:
                memo[i][i+1] = True
                ans += 1
        
        for _len in range(3, N+1):
            for i in range(N- _len+1):
                if s[i] == s[i + _len-1] and memo[i+1][i + _len-2]:
                    memo[i][i + _len-1] = True
                    ans += 1
       
        return ans
