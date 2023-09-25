class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = sorted(s), sorted(t)
        for i, val in enumerate(s):
            if val != t[i]:
                return t[i]
        return t[-1]