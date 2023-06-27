class Solution:
    def findPoisonedDuration(self, ts: List[int], duration: int) -> int:
        total_time = duration * len(ts)

        for i in range(1, len(ts)):
            diff = ts[i] - ts[i-1]
            if diff <= duration:
                total_time -= duration - diff
        
        return total_time