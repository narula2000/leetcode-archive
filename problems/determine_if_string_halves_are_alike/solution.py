class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        a, b = s[:mid], s[mid:]
        return self.countVowels(a) == self.countVowels(b)
        
    
    def countVowels(self, string):
        vowels = set("aeiou")
        return sum(1 for char in string.lower() if char in vowels)