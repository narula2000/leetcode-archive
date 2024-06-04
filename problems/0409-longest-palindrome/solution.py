class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        ans = 0
        for char in s:
            if char in seen:
                seen.remove(char)
                ans += 2
            else:
                seen.add(char)
        return  ans + 1 if seen else ans
