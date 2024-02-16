class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        result = sorted(arr, key=lambda x: (count[x], x))
        return len(set(result[k:]))