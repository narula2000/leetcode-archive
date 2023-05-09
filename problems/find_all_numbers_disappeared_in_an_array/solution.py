class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        given = set(nums)
        result = []
        for i in range(1, len(nums)+1):
            if i not in given:
                result.append(i)
        
        return result