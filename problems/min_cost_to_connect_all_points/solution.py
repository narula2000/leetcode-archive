class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        hash = dict()

        for i, (x, y) in enumerate(points):
            if i:
                hash[(x, y)] = float('inf')
            else:
                hash[(x, y)] = 0

        res = 0 
        while hash:
            x, y = min(hash, key=hash.get)
            res += hash.pop((x, y))

            for x_1, y_1 in hash:
                hash[(x_1, y_1)] = min(hash[x_1, y_1], abs(x - x_1) + abs(y - y_1))
        
        return res
