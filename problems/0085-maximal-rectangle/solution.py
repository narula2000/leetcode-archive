class Solution:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        M, N = len(mat), len(mat[0])
        memo = [[0] * N for _ in range(M)]

        for i in range(M):
            memo[i][0] = 1 if mat[i][0] == '1' else 0
        
        for i in range(M):
            for j in range(1, N):
                if mat[i][j] == '1':
                    if memo[i][j - 1]:
                        memo[i][j] = memo[i][j - 1] + 1
                    else:
                        memo[i][j] = 1
        
        ans = 0
        for j in range(N):
            col = []
            for i in range(M):
                col.append(memo[i][j])

            for ptr in range(len(col)):
                left, right = ptr, ptr
                val = col[ptr]
    
                cnt = 1
                while left >= 0 and col[left] >= val:
                    if left != ptr:
                        cnt += 1
                    left -= 1
                while right < len(col) and col[right] >= val:
                    if right != ptr:
                        cnt += 1
                    right += 1
                
                ans = max(ans, val * cnt)
        return ans
