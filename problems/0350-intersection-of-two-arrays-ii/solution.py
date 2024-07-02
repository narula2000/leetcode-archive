class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = [0] * 1001
        result = []
        for num in nums1:
            arr[num] += 1

        for num in nums2:
            if arr[num] > 0:
                result.append(num)
                arr[num] -= 1

        return result[: len(result)] 
