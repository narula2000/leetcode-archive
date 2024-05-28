class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start, curr, ans = 0, 0, 0

        for end in range(len(s)):
            curr += abs(ord(s[end]) - ord(t[end]))

            while curr > maxCost:
                curr -= abs(ord(s[start]) - ord(t[start]))
                start += 1

            ans = max(ans, end - start + 1)
        
        return ans
