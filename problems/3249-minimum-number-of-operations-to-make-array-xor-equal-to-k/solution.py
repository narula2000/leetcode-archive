class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        tmp = 0
        for i in nums:
            tmp ^= i
        tmp ^= k
        return bin(tmp).count('1') 
