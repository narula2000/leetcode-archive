class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result, prev = 0, float('-inf')

        for left, right in intervals:
            if left < prev:
                result += 1
                if right > prev:
                    continue
            
            prev = right
        
        return result