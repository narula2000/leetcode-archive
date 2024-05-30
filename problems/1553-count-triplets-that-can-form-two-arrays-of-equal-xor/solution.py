class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0 
        for i in range(len(arr)):
            val = arr[i]
            for j in range(i+1, len(arr)):
                val ^= arr[j]
                if val == 0: ans += (j - i)
        return ans
