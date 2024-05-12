class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(1, len(grid)-1):
            tmp = []
            for j in range(1, len(grid)-1):
                _max = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        _max = max(_max, grid[k][l])
                tmp.append(_max)
            res.append(tmp)
        return res 
