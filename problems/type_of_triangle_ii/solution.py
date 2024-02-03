class Solution:
    def triangleType(self, nums: List[int]) -> str:
        count = Counter(nums)
        
        if len(count.keys()) == 1:
            return "equilateral"
        elif len(count.keys()) == 2:
            dup = 0
            single = 0
            for k, v in count.items():
                if v == 2:
                    dup = k
                if v == 1:
                    single = k
            if dup*2 > single:
                return "isosceles"
            
            return "none"
        else:
            max_side = max(nums)
            tmp = 0
            for num in nums:
                if num != max_side:
                    tmp += num
            if tmp > max_side:
                return "scalene"
            
            return "none"
        