class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total, count = 0, 0
        _min, _max = float("inf"), float("-inf")

        for num in nums:
            total += num
            change = (num ^ k) - num

            if change > 0:
                _min = min(_min, change)
                total += change
                count += 1
            else:
                _max = max(_max, change)

        if count % 2 == 0:
            return total

        return max(total - _min, total + _max)
 
