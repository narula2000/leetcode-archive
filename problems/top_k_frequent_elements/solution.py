class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        N = len(nums)
        freqs = [[] for _ in range(N+1)]

        for num, count in count.items():
            freqs[count].append(num) # Aggregate all number of that freq

        ans = [] 
        for i in range(N, 0, -1):
            for num in freqs[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans


        
