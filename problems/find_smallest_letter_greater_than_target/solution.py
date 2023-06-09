class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)-1

        while l <= r:
            mid = (l+r) // 2
            if letters[mid] <= target: # shift right
                l = mid + 1
            else: # shift left
                r = mid - 1
        
        if l == len(letters):
            return letters[0]
        
        return letters[l]  

"""
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]
"""