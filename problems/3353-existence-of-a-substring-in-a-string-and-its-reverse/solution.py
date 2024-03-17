class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        _set = set()
        for i in range(len(s) - 1):
            _set.add(s[i:i+2])

        reverse = s[::-1]
        for i in range(len(s) - 1):
            if reverse[i:i+2] in _set:
                return True
        
        return False
            
