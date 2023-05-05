class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        i, j = 0, 0

        max_v = 0
        counter = 0

        while j < len(s):
            if s[j] in vowels:
                counter += 1
            
            if j - i >= k:
                if s[i] in vowels:
                    counter -= 1
                i += 1

            j += 1
            max_v = max(max_v, counter)

        return max_v

"""
class EditorialSolution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Build the window of size k, count the number of vowels it contains.
        count = 0
        for i in range(k):
            count += int(s[i] in vowels)
        answer = count
        
        # Slide the window to the right, focus on the added character and the
        # removed character and update "count". Record the largest "count".
        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i - k] in vowels)
            answer = max(answer, count)
        
        return answer
"""