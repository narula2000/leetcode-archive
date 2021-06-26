class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        for ele in S:
            if ele == ')':
                val = stack.pop() if stack else False
                if val != '(':
                    return False
            elif ele == ']':
                val = stack.pop() if stack else False
                if val != '[':
                    return False
            elif ele == '}':
                val = stack.pop() if stack else False
                if val != '{':
                    return False
            else:
                stack.append(ele)
        if len(stack) > 0:
            return False
        else:
            return True
            
            
        