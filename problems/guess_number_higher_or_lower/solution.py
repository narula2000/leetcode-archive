# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        my_guess = (low + high) >> 1
        
        while (result := guess(my_guess)) != 0:
            if result == 1:
                low = my_guess + 1
            else:
                high = my_guess - 1
            
            my_guess = (low + high) >> 1
        
        return my_guess