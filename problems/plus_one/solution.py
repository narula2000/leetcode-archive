class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1
        plus_one = False
        digits[-1] += 1
        while idx > 0:
            if plus_one:
                plus_one = False
                digits[idx] += 1
            if digits[idx] > 9:
                plus_one = True
                digits[idx] = digits[idx] % 10
            idx -= 1
        if plus_one:
            digits[0] += 1
        if digits[0] > 9:
            digits[0] = digits[0] % 10
            digits = [1] + digits
 
        return digits

"""
class EditorialSolution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # move along the input array starting from the end
        for i in range(n):
            idx = n - 1 - i
            # set all the nines at the end of array to zeros
            if digits[idx] == 9:
                digits[idx] = 0
            # here we have the rightmost not-nine
            else:
                # increase this rightmost not-nine by 1
                digits[idx] += 1
                # and the job is done
                return digits

        # we're here because all the digits are nines
        return [1] + digits
"""