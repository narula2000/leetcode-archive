class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_1, hash_2 = dict(), dict()

        for num in nums1:
            if num in hash_1:
                hash_1[num] += 1
            else:
                hash_1[num] = 1

        for num in nums2:
            if num in hash_2:
                hash_2[num] += 1
            else:
                hash_2[num] = 1

        result = [] 
        for key, count in hash_1.items():
            if key in hash_2:
                count = min(count, hash_2[key])
                for _ in range(count):
                    result.append(key)
        return result