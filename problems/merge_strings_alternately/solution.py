class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        n, m = len(word1), len(word2)
        result = ""
        switch = False
        while i < n and j < m:
            if switch:
                result += word2[j]
                j += 1
                switch = False
            result += word1[i]
            i += 1
            switch = True

        while i < n:
            result += word1[i]
            i += 1

        while j < m:
            result += word2[j]
            j += 1
        
        return result

"""
class EditorialSolution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        n = max(len(word1), len(word2))
        for i in range(n):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]

        return "".join(result)
        
class EditorialSolution(object):
    def mergeAlternately(self, word1, word2):
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        result = []

        while i < m or j < n:
            if i < m:
                result += word1[i]
                i += 1
            if j < n:
                result += word2[j]
                j += 1

        return "".join(result)
"""