class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [], []
        
        for num in nums:
            if len(arr1) == 0:
                arr1.append(num)
                continue
            elif len(arr2) == 0:
                arr2.append(num)
                continue
            else:
                if arr1[-1] > arr2[-1]:
                    arr1.append(num)
                else:
                    arr2.append(num)
        
        ans = []
        ans.extend(arr1)
        ans.extend(arr2)
        return ans