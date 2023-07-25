class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]: # Peak is to the left
                right = mid
            else: # Peak is to the right
                left = mid + 1
                
        return right
        
"""
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if arr[i+1] < arr[i]:
                return i
"""