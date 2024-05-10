class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                heappush(heap, (arr[i]/arr[j], (arr[i], arr[j])))
        
        for _ in range(k-1):
            heappop(heap)
            
        return heappop(heap)[1]

