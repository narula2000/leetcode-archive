class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort()
        prev = points[0]
        total = 1
        for i in range(1, len(points)):
            start, end = points[i]
            if start > prev[1]:
                total += 1
                prev = [start, end]
            else:
                prev[1] = min(prev[1], end)
        
        return total
