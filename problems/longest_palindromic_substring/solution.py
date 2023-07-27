class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        N = len(s)
        hash = [[0] * N for _ in range(N)]

        for i in range(N):
            hash[i][i] = True
            result = s[i]
        
        for i in range(N-1, -1, -1):
            for j in range(i+1, N):
                if s[i] == s[j]:
                    if j - i == 1 or hash[i + 1][j - 1]:
                        hash[i][j] = True
                        if len(result) < len(s[i:j + 1]):
                            result = s[i:j + 1]
        
        return result