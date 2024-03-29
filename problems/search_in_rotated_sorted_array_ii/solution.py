class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[right]:
                right -= 1 # Fail to get sorted side
            elif nums[mid] > nums[right]:
                if nums[left] <= target and target < nums[mid]: # In between
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[right] >= target and target > nums[mid]: # In between
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False