class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        total_length = n + m
        middle = total_length // 2
        isEven = False
        if total_length % 2 == 0:
            isEven = True
        i, j, count = 0, 0, -1
        curr, prev = None, None
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
            count += 1
            if count == middle and not isEven:
                return curr
            if isEven and count == middle - 1:
                if i == n:
                    return (curr + nums2[j]) / 2
                elif j == m:
                    return (curr + nums1[i]) / 2
                else:
                    return (curr + min(nums1[i], nums2[j])) / 2
            prev = curr

        while i < n:
            curr = nums1[i]
            i += 1
            count += 1
            if count == middle and not isEven:
                return curr
            if count == middle and isEven:
                return (curr + prev) / 2
            prev = curr

        while j < m:
            curr = nums2[j]
            j += 1
            count += 1
            if count == middle and not isEven:
                return curr
            if count == middle and isEven:
                return (curr + prev) / 2
            prev = curr
        return -1
