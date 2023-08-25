class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M, N, L = len(s1), len(s2), len(s3)

        if M + N != L:
            return False

        memo = dict()

        def helper(i, j, k):
            if k == L:
                return True
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = False

            if i < M and s1[i] == s3[k]:
                res = res or helper(i+1, j, k+1)

            if j < N and s2[j] == s3[k]:
                res = res or helper(i, j+1, k+1)
            
            memo[(i, j)] = res

            return res
        
        return helper(0, 0, 0)