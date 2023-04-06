class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        visited = dict()
        for char in s:
            if char in visited:
                visited[char] += 1
            else:
                visited[char] = 1
        for char in t:
            if char not in visited:
                return False
            elif visited[char] == 0:
                return False
            else:
                visited[char] -= 1
        return True