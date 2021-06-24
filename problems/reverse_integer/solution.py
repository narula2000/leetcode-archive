class Solution:
    def reverse(self, x: int) -> int:
        stringInt = str(x)
        answerString = ""
        for unit in stringInt:
            answerString = unit + answerString
        if (answerString[-1] == "-"):
            answerString = "-" + answerString[:-1]
        answerInt = int(answerString)
        isAnswerInRange = (-2**31 <= answerInt) and (answerInt <= 2**31 - 1)
        if (isAnswerInRange):
            return answerInt
        else:
            return 0
        