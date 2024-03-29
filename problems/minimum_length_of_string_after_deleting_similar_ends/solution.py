class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        
        while left < right and s[left] == s[right]:
            char = s[left]
            while left <= right and s[left] == char: # Prefix
                left += 1
            while right >= left and s[right] == char: # Suffix
                right -= 1
        
        return right - left + 1 