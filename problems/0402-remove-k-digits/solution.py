class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        stack = []
        for num in nums:
            while k > 0 and stack and stack[-1] > num:
                k -= 1
                stack.pop()
            stack.append(num)
        stack = stack[:len(stack) - k]
        ans = "".join(stack)
        for i in range(len(ans)):
            if ans[i] != "0":
                return ans[i:]
        return "0"
