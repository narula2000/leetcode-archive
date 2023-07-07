class Solution:
    def longestPalindrome(self, s: str) -> int:
        _set = set()
        for char in s:
            if char in _set:
                _set.remove(char)
            else:
                _set.add(char)
        
        if len(_set) == 0:
            return len(s)
        else:
            return len(s) - len(_set) + 1