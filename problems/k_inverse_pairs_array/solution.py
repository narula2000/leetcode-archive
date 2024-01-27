class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        M = 10**9 + 7
        memo = [0] + [1] * (k + 1)
        for i in range(2, n + 1):
            tmp = [0]
            for j in range(k + 1):
                val = memo[j + 1]
                val -= memo[j - i + 1] if j >= i else 0
                tmp.append((tmp[-1] + val) % M)
            memo = tmp
        return (memo[k + 1] - memo[k]) % M