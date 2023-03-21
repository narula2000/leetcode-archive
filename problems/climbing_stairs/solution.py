class Solution:
    def climbStairs(self, n: int) -> int:
        hash = dict()
        hash[1] = 1
        hash[2] = 2
        def helper(num):
            if num in hash:
                return hash[num]
            else:
                hash[num] = helper(num-1) + helper(num-2)
                return hash[num]
        return helper(n)