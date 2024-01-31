class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        ans = [0] * len(temps)
        stack = []
        for i, temp in enumerate(temps):
            while stack and stack[-1][0] < temp: # If current temp is greater than previous temp
                temp_val, idx = stack.pop()
                ans[idx] = i - idx
            
            stack.append([temp, i])
        
        return ans

