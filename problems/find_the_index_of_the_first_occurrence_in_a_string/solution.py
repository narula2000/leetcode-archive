class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay_idx, seen = 0, 0
        n_hay, n_needle = len(haystack), len(needle)
        while hay_idx < len(haystack):
            if haystack[hay_idx] == needle[0]:
                if n_hay - hay_idx < n_needle:
                    return -1
                counter = 0
                for i in range(n_needle):
                    if needle[i] == haystack[i+hay_idx]:
                        counter +=1
                if counter == n_needle:
                    return seen
            hay_idx += 1
            seen = hay_idx
        return -1

"""
class EditorialSolution::
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        for window_start in range(n - m + 1):
            for i in range(m):
                if needle[i] != haystack[window_start + i]:
                    break
                if i == m - 1:
                    return window_start

        return -1
"""