class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        que = deque(range(1, 10))
        ans = []

        while que:
            val = que.popleft()
            if low <= val <= high:
                ans.append(val)
            if val > high:
                return ans
            if (val % 10) < 9: # We will skip 9 because it will increase the digit infront
                que.append((val * 10) + (val % 10) + 1)
        
        return ans