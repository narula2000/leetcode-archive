class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        print(counter)
        ans = []
        for key, val in counter.items():
            if val == 1:
                print(key, val)
                ans.append(key)
        return ans
                
