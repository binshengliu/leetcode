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

        origin = [row[:] for row in matrix]

        for row in range(rows):
            for col in range(cols):
                matrix[col][cols-row-1] = origin[row][col]
