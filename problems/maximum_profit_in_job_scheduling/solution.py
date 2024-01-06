class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profits: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profits))
        endTimes, N = [e for e, s, p in jobs], len(jobs)
        memo = [0] * N
        memo[0] = jobs[0][2] # Set first idx to first job

        for i in range(1, N):
            start = jobs[i][1]
            end = jobs[i][0]
            profit = jobs[i][2]

            memo[i] = memo[i - 1] # Haven't schdule job

            idx = bisect.bisect_right(endTimes, start) - 1
            job = memo[idx]
            if idx < 0:
                job = 0
            
            memo[i] = max(memo[i], job + profit)

        
        return memo[-1]
