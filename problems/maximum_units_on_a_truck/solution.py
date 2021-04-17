class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        for boxes, unit in boxTypes:
            if truckSize > boxes:
                truckSize -= boxes
                ans += boxes * unit
            else:
                ans += truckSize * unit
                return ans
        return ans

        