class Solution:
    def convertToTitle(self, col: int) -> str:
        result = ""
        buffer_limit = ord('A')

        while col > 0:
            result = chr(buffer_limit + (col - 1) % 26) + result
            col = (col - 1) // 26
        
        return result