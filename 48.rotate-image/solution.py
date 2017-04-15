# 1 2 3
# 4 5 6
# 7 8 9

# first swap rows vertically =>

# 7 8 9
# 4 5 6
# 1 2 3

# then swap elements diagnoally =>

# 7 4 1
# 8 5 2
# 9 6 3


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        if rows != cols:
            return

        for row in range(int(rows / 2)):
            matrix[row], matrix[rows-row-1] = matrix[rows-row-1], matrix[row]

        for row in range(rows):
            for col in range(row+1, cols):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
