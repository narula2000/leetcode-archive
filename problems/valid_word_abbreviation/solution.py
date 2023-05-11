class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        while i < len(word) and j < len(abbr): 
            if abbr[j].isalpha(): 
                if word[i] == abbr[j]:
                    i, j = i+1, j+1
                else:
                    return False 
            else: 
                if abbr[j] == "0":
                    return False
                start = j 
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                i += int(abbr[start:j])
        return i == len(word) and j == len(abbr)
