class Solution:
    def firstUniqChar(self, s: str) -> int:
        for idx, char in enumerate(s):
            if s.find(char) == s.rfind(char):
                return idx
        return -1