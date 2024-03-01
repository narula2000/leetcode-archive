class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_of_1 = s.count('1')
        count_of_0 = s.count('0')
        return ('1' * (count_of_1 - 1)) + ('0' *  count_of_0) + '1'