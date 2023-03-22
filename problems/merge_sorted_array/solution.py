class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr_1, ptr_2 = m - 1, n - 1
        total_length = n + m
        for ptr in range(total_length - 1, -1, -1):
            if ptr_2 < 0:
                break
            if ptr_1 >= 0 and nums1[ptr_1] > nums2[ptr_2]:
                nums1[ptr] = nums1[ptr_1]
                ptr_1 -= 1
            else: # This order because if nums1 is done we need to keep adding nums2 to it
                nums1[ptr] = nums2[ptr_2]
                ptr_2 -= 1
