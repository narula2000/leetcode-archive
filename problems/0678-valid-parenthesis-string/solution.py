class Solution:
    def checkValidString(self, s: str) -> bool:
        _min, _max = 0, 0
        for char in s:
            if char == "(":
                _min += 1
                _max += 1
            elif char == ")":
                _min -= 1
                _max -= 1
            else:
                _min -= 1
                _max += 1
            if _max < 0:
                return False
            if _min < 0:
                _min = 0
        return _min == 0

