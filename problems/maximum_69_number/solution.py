class Solution:
    def maximum69Number (self, num: int) -> int:
        num_lst = list(str(num))
        for idx, char in enumerate(num_lst):
            if char == '6':
                num_lst[idx] = '9'
                break

        return int("".join(num_lst))