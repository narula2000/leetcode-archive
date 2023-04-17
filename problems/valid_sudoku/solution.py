class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check Row
        for row in board:
            visited = set()
            for val in row:
                if val == ".":
                    continue
                if val in visited:
                    return False
                visited.add(val)
        
        # Check Col
        for col_num in range(9):
            visited = set()
            col = [row[col_num] for row in board]
            for val in col:
                if val == ".":
                    continue
                if val in visited:
                    return False
                visited.add(val)

        # Check Box
        for i in (0,3,6):
            for j in (0,3,6):
                square = [board[x][y] for x in range(i,i+3) 
                                        for y in range(j,j+3)]
                visited = set()
                for val in square:
                    if val == ".":
                        continue
                    if val in visited:
                        return False
                    visited.add(val)
        return True