class Solution:
    def minSpeedOnTime(self, distance: List[int], hour: float) -> int:
        def can_reach(speed):
            curr = 0
            for i in range(len(distance) - 1):
                curr += math.ceil(distance[i] / speed) # Round up
                if curr > hour: # Can't reach office in time
                    return False
            return (curr + (distance[-1] / speed)) <= hour # Check for last train
        
        left, right = 1, 10**7
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if can_reach(mid):
                result = mid
                right = mid - 1 # Find answer on the left
            else:
                left = mid + 1 # Find answer on the right
        
        return result