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

            