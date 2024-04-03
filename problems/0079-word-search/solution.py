class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, k):
            if k == len(word): return True
            i_in_board = i < 0 or i >= len(board)
            j_in_board = j <0 or j >= len(board[0])
            if i_in_board or j_in_board or board[i][j] != word[k]: return False

            tmp = board[i][j]
            board[i][j] = ""


            up = backtrack(i + 1, j, k + 1)
            down = backtrack(i - 1, j, k+ 1)
            left = backtrack(i, j + 1, k+ 1)
            right = backtrack(i, j - 1, k+ 1)

            if up or down or left or right: return True

            board[i][j] = tmp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0): return True
        return False
