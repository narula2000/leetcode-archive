class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        hash = dict()
        for i, char in enumerate(s):
            hash[char] = i

        res = []

        for i, char in enumerate(s):
            if char not in res:
                while res and i < hash[res[-1]] and char < res[-1]:
                    res.pop()
            
                res.append(char)
        
        return "".join(res)