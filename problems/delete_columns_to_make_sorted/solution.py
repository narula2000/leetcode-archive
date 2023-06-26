class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        transpose = list(zip(*strs))
        result = 0
        for col in transpose:
            old = list(col)
            old.sort()
            if old != list(col):
                result += 1
        return result