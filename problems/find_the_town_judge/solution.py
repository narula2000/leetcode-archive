class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tmp = [0] * (n+1)

        for trustee, trusted in trust:
            tmp[trustee] -= 1
            tmp[trusted] += 1

        for i in range(1, n+1):
            if tmp[i] == n-1:
                return i

        return -1 