class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s, map_t = dict(), dict()
        for char_s, char_t in zip(s, t):
            if char_s in map_s:
                if map_s[char_s] != char_t:
                    return False
            else:
                if char_t in map_t:
                    return False
                
                map_s[char_s] = char_t
                map_t[char_t] = char_s
        return True

