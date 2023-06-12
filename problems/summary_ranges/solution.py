class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start, end, N = 0, 0, len(nums)
        result = []

        while start < N and end < N:
            if end+1 < N and nums[end]+1 == nums[end+1]:
                end += 1
            else:
                if start == end:
                    result.append(str(nums[start]))
                    start += 1
                else:
                    result.append(f'{nums[start]}->{nums[end]}')
                    start = end + 1
                end  += 1
        return result