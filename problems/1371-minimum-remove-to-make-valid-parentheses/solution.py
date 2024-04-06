class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left, right, stack = 0, 0, []

        for char in s:
            if char == "(":
                left += 1
            elif char == ")":
                right += 1
            if right > left:
                right -= 1
            else:
                stack.append(char)
        
        answer = ""
        while stack:
            curr = stack.pop()
            if left > right and curr =="(":
                left -= 1
            else:
                answer += curr
        return answer[::-1]
        
