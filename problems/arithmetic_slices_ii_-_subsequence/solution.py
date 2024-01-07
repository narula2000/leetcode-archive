class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0  
        memo = [defaultdict(int) for _ in range(N)]

        for i in range(1, N):
            for j in range(i):
                diff = nums[i] - nums[j]
                memo[i][diff] += 1  
                if diff in memo[j]:
                    memo[i][diff] += memo[j][diff]
                    ans += memo[j][diff]

        return ans 