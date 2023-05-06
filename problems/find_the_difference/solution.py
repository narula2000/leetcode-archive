from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash_s = Counter(s)
        hash_t = Counter(t)

        for key, val in hash_t.items():
            if key not in hash_s:
                return key
            else:
                if val != hash_s[key]:
                    return key
        
        return ""