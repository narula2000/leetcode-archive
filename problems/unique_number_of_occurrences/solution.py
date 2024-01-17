class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        occur = set()
        for val in counter.values():
            if val in occur:
                return False
            occur.add(val)
        
        return True