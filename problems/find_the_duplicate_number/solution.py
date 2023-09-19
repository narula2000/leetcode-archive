class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums) - 1
        visited = [False] * (N + 1)
        for num in nums:
            if visited[num]:
                return num
            visited[num] = True
        return -1