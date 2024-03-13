class Solution:
    def pivotInteger(self, n: int) -> int:
        sum_till_n = sum(i for i in range(1, n+1))
        tmp = 0

        for i in range(1, n+1):
            tmp += i
            if 2 * tmp == sum_till_n + i:
                return i
        return -1
