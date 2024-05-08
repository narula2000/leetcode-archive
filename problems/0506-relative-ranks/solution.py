class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        answer = [0] * len(score)
        heap = []
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        for i, scr in enumerate(score):
            heappush(heap, (-scr, i))

        num = 1
        while heap:
            scr, idx = heappop(heap)
            if num < 4:
                answer[idx] = rank[num - 1]
            else:
                answer[idx] = str(num)
            num += 1
        return answer
