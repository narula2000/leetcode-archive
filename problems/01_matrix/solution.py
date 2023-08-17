class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        que = deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    que.append((i,j))
                else:
                    matrix[i][j] = -1
        
        while que:
            x, y = que.popleft()
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for row, col in directions:
                new_x, new_y = x + row, y + col
                in_range = 0 <= new_x <= len(matrix) - 1 and 0 <= new_y <= len(matrix[0]) - 1
                if  in_range and matrix[new_x][new_y] == -1:
                    matrix[new_x][new_y] = matrix[x][y] + 1
                    que.append((new_x, new_y))
        
        return matrix
