class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        maxs = list(counter.values())
        maxs.sort(reverse=True)

        k_s = set(maxs[:k])

        result = []
        for key, val in counter.items():
            if val in k_s:
                result.append(key)

        return result

"""
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 
"""