class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []
        length = len(apples)
        ans = 0
        day = 0
        while day < length or heap:
            if day < length and apples[day] > 0:
                exp_date = day + days[day]
                heapq.heappush(heap, (exp_date, apples[day]))
            while heap:
                exp_date, apple = heapq.heappop(heap)
                if exp_date > day:
                    ans += 1
                    apple -= 1
                    if apple > 0:
                        heapq.heappush(heap, (exp_date, apple))
                    break
            day += 1
        return ans



        