class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        buffer = []
        result = 0
        for num in nums:
            if num != val:
                result += 1
                buffer.append(num)
        for i in range(len(buffer)):
            nums[i] = buffer[i]
        return result

"""
class OtherSolution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx
"""