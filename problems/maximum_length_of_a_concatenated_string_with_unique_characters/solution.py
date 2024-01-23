class Solution:
    def maxLength(self, arr: List[str]) -> int:
        memo = [set()]
        for chars in arr:
            chars_set = set(chars)
            if len(chars_set) < len(chars): # Skip chars with duplicate
                continue
            
            for i in range(len(memo)):
                union = memo[i]
                if chars_set & union: # Skip if there is intersection
                    continue
                memo.append(chars_set | union)
            
        return max(len(val) for val in memo)
