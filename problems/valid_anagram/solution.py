class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_s, c_t = Counter(s), Counter(t)
        
        if c_s.keys() != c_t.keys():
            return False

        for k, v in c_t.items():
            if k not in c_s.keys():
                return False
            if c_s[k] != c_t[k]:
                return False
        return True
