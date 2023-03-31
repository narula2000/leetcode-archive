class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alpha = ['A', 'B', 'C', 'D'
                , 'E', 'F', 'G', 'H'
                , 'I', 'J', 'K', 'L'
                , 'M', 'N', 'O', 'P'
                , 'Q', 'R', 'S', 'T'
                , 'U', 'V', 'W', 'X'
                , 'Y', 'Z']
        column = columnTitle[::-1]
        result = 0
        for i, char in enumerate(column):
            unit = ((alpha.index(char)+1) * 26**i)
            result += unit
        return result

"""
class EditorialSolution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        n = len(s)
        for i in range(n):
            result = result * 26
            result += (ord(s[i]) - ord('A') + 1)
        return result
"""