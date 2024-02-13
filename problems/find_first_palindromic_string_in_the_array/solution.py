class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(string):
            left, right = 0, len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        for word in words:
            if is_palindrome(word):
                return word
        return ""