class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []

        def backtrace(ans, _digits):
            if not _digits:
                result.append(ans)
                return
            
            for letter in phone[_digits[0]]:
                backtrace(ans + letter,  _digits[1:]) # Shift to right
        
        backtrace("", digits)

        return result