class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        idx = 0
        middle = len(s) // 2
        while idx < middle:
            s[idx], s[-idx - 1] = s[-idx - 1], s[idx]
            idx += 1