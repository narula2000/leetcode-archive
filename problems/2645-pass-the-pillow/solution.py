class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        N = 2 * n-2
        x = time % N
        return 1+x if x < n else N+1 - x
