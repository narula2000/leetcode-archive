class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter, ans  = Counter(arr1), []
        for num in arr2:
            if num in counter:
                ans.extend([num]*counter[num])
                del counter[num]
        for num in sorted(counter.keys()):
            ans.extend([num]*counter[num])
        return ans
