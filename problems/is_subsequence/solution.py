class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = counter = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                counter += 1
                i += 1
            j += 1

        return counter == len(s)