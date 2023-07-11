class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for idx in range(len(nums)):
            if idx != 0 and nums[idx] == nums[idx-1]: # Avoid triplets
                continue
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                _sum = nums[left] + nums[right]
                
                if _sum < -nums[idx]:
                    left += 1
                elif _sum > -nums[idx]:
                    right -= 1
                else:
                    result.append([nums[idx], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            
        return result