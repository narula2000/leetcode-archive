class Solution:
    hash = {0:0, 1:1, 2:1}

    def fib(self, n: int) -> int:
        if n in self.hash.keys():
            return self.hash[n]
        else:
            self.hash[n] = self.fib(n-2) + self.fib(n-1)
            return self.hash[n]