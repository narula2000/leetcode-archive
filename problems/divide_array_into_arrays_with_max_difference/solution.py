class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(0, len(nums), 3):
            head, mid, tail = nums[i:i+3]

            if tail - head > k:
                return []
            
            result.append([head, mid, tail])
        return result