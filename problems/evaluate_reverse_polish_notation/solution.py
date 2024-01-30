class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "*": lambda a,b: a*b,
            "/": lambda a,b: int(a/b),
        }

        for token in tokens:
            if token in operations.keys():
                num, operation  = stack.pop(), operations[token]
                stack[-1] = operation(stack[-1], num)
                continue
                
            stack.append(int(token))

        return stack[0]