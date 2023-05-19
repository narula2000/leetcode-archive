class Solution:
    def checkStraightLine(self, coord: List[List[int]]) -> bool:
        x_1, y_1 = coord[0]
        x_2, y_2 = coord[1]

        rise = y_2 - y_1
        run = x_2 - x_1

        if run == 0:
            for x, y in coord:
                if x != x_1:
                    return False
            return True

        if rise == 0:
            for x, y in coord:
                if y != y_1:
                    return False
            return True


        gradient = rise / run
        constant = y_1 - (gradient*x_1)

        for x, y in coord[1:]:
            if constant != y - (gradient*x):
                return False
        
        return True