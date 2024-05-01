class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = 0 
        while i <= len(word):
            if i == len(word):
                return word
            if word[i] == ch:
                break
            i += 1

        letters, left, right = list(word), 0, i
        while left < right:
            letters[left], letters[right] = letters[right], letters[left]
            left += 1
            right -= 1
        
        return "".join(letters)

