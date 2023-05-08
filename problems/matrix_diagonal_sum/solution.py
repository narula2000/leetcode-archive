class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result  = 0
        N = len(mat)
        for i in range(len(mat)):
            result += mat[i][i]
            result += mat[N-1-i][i]
        
        if N % 2 != 0:
            mid = int(N/2)
            result -= mat[mid][mid]
            
        return result 