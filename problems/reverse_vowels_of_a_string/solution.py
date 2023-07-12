class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        while left < right:
            if s[left].lower() in vowels and s[right].lower() in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left].lower() not in vowels:
                left += 1
            elif s[right].lower() not in vowels:
                right -= 1
        return "".join(s)
            

            