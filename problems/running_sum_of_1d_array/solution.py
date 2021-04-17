class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tmp = 0
        answer = []
        for num in nums:
            tmp += num
            answer.append(tmp)
        return answer
