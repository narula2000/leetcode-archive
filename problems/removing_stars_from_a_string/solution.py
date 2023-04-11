class Solution:
    def removeStars(self, s: str) -> str:
        buffer, right = 0, len(s) - 1
        result = ""
        while right > -1:
            char = s[right]
            if char == "*":
                buffer += 1
            else:
                if buffer == 0:
                    result = char + result
                else:
                    buffer -= 1
            right -= 1
        return result

"""
class EditorialSolution:
    def removeStars(self, s):
        st = []
        for i in range(len(s)):
            if s[i] == '*':
                st.pop()
            else:
                st.append(s[i])

        return ''.join(st)
"""