class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        memo = [0] * (N+1)

        for i in range(N):
            _max, _sum = 0, 0
            for j in range(i, max(-1, i-k), -1):
                _max = arr[j] if _max < arr[j] else _max
                curr = _max * (i-j + 1) + memo[j]
                _sum = curr if _sum < curr else _sum
            
            memo[i+1] = _sum
        
        return memo[-1]
