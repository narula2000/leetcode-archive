class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def string_to_int(string):
            int_dict = {
                '0': 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4,
                '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9
            }
            result  = 0

            for char in string:
                result *= 10
                result += int_dict[char]
            
            return result
        num = string_to_int(num1) + string_to_int(num2)

        if num == 0:
            return '0'

        s = []

        while num:
            s.append(chr(48 + num % 10))
            num = num // 10

        ans = "".join(reversed(s))
        return ans