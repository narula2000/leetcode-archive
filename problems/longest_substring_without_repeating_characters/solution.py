class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        iPointer = 0
        jPointer = 0
        window = set()
        ans = 0
        while (jPointer < len(s)):
            if ( s[jPointer] not in window ):
                window.add(s[jPointer])
                jPointer += 1
                ans = max(len(window),ans)
            else:
                window.remove(s[iPointer])
                iPointer += 1
        return ans
                