class Solution:
    def minFallingPathSum(self, g: List[List[int]]) -> int:
        for i in range(1, len(g)):
            tmp =  sorted(g[i-1])
            for j in range(len(g)):
                if g[i-1][j] == tmp[0]:
                    g[i][j] += tmp[1]
                else:
                    g[i][j] += tmp[0]
        return min(g[-1]) 
