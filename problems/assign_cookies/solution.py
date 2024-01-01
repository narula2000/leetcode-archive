class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if s == []:
            return 0

        g.sort()
        s.sort()

        answer = 0
        cookie_i =  len(s) - 1
        child_i = len(g) - 1
        while cookie_i >= 0 and child_i >= 0:
            if s[cookie_i] >= g[child_i]:
                answer += 1
                cookie_i -= 1
                child_i -= 1
            else:
                child_i -= 1

        return answer
