class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        answer = None
        for word in words:
            if word != "":
                answer = word
        return len(answer)

"""
class OtherSolution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split().pop())
"""