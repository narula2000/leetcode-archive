class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = dict()

        for char in ransomNote:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        
        for char in magazine:
            if char in counter:
                counter[char] -= 1

        for _, val in counter.items():
            if val > 0:
                return False
        
        return True