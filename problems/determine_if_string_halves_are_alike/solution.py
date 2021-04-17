class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        middle = int(len(s) / 2)
        a = s[:middle]
        b = s[middle:]

        counterA = 0
        for char in a:
            if char in vowels:
                counterA += 1
        counterB = 0
        for char in b:
            if char in vowels:
                counterB += 1

        return counterA == counterB
        