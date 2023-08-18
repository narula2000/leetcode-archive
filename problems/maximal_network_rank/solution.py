class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        result = 0
        hash = {i:set() for i in range(n)} # Create hash map of key(i) -> value(set())

        for a, b in roads:
            hash[a].add(b)
            hash[b].add(a)
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                value = len(hash[i]) + len(hash[j]) - (j in hash[i])
                result = max(result, value)
        return result