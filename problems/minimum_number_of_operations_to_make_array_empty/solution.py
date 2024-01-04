class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        if min(counts.values()) == 1:
            return -1

        ans = 0 
        for count in counts.values():
            ans += math.ceil(count / 3.0)

        return int(ans)

            