class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1], [1, 1]]

        for i in range(2, rowIndex + 1):
            row = [1] * (i + 1)

            for j in range(1, len(row) - 1):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle[rowIndex]
 
