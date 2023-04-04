class Solution:
    def partitionString(self, s: str) -> int:
        visited = set()
        result = 1
        for char in s:
            if char in visited:
                result += 1
                visited = set()
            visited.add(char)
        return result