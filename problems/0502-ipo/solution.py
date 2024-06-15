class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        projects.sort()
        heap, i = [], 0
        for _ in range(k):
            while i < len(profits) and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1
            if not heap:
                break
            w -= heapq.heappop(heap)
        return w
