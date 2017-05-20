class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        rows = len(matrix)
        cols = len(matrix[0])

        rows_to_zero = []
        cols_to_zero = []

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    rows_to_zero.append(row)
                    cols_to_zero.append(col)

        for row in rows_to_zero:
            for col in range(cols):
                matrix[row][col] = 0

        for row in range(rows):
            for col in cols_to_zero:
                matrix[row][col] = 0
