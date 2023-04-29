class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cypher = dict()
        for i, char in enumerate(s):
            if char in cypher:
                if cypher[char] != t[i]:
                    return False
            else:
                if t[i] in cypher.values():
                    return False
                cypher[char] = t[i]
        return True

"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
"""