class MyQueue:

    def __init__(self):
        self.ins = []
        self.outs = []

    def push(self, x: int) -> None:
        self.ins.append(x)        

    def pop(self) -> int:
       self.peek()
       return self.outs.pop() 

    def peek(self) -> int:
        if not self.outs:
            while self.ins:
                self.outs.append(self.ins.pop())        
        return self.outs[-1]

    def empty(self) -> bool:
        return  not (self.ins or self.outs)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()