class Solution:
    def countKeyChanges(self, s: str) -> int:
        string = s.lower()
        prev, counter = string[0], 0
        for i in range(1, len(string)):
            if prev != string[i]:
                counter += 1
            prev = string[i]
        
        return counter
        