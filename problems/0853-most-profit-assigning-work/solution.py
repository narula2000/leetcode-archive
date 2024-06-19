class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        tmp = [(difficulty[i], profit[i]) for i in range(len(difficulty))]
        tmp.sort()
        worker.sort()
        ans, j, best = 0, 0, 0 
        for w in worker:
            while j < len(worker) and w >= tmp[j][0]:
                best = max(best, tmp[j][1])
                j += 1
            ans += best
        return ans

