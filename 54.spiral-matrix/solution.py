class Solution(object):
    _LEFT = 0
    _RIGHT = 1
    _DOWN = 2
    _UP = 3
    _OCCUPIED = '.'

    def _spiralOrderRecursively(self, matrix, row, col, direction, ans):
        """row and col must be valid"""
        ans.append(matrix[row][col])
        matrix[row][col] = self._OCCUPIED
        if direction == self._RIGHT:
            if col + 1 < len(matrix[0]) and matrix[row][col+1] != self._OCCUPIED:
                self._spiralOrderRecursively(matrix, row, col+1, self._RIGHT, ans)
            elif row + 1 < len(matrix) and matrix[row+1][col] != self._OCCUPIED:
                self._spiralOrderRecursively(matrix, row+1, col, self._DOWN, ans)
            else:
                return
        elif direction == self._DOWN:
            if row + 1 < len(matrix) and matrix[row+1][col] != self._OCCUPIED:
                self._spiralOrderRecursively(matrix, row+1, col, self._DOWN, ans)
            elif 0 <= col - 1 and matrix[row][col-1] != self._OCCUPIED:
                self._spiralOrderRecursively(matrix, row, col-1, self._LEFT, ans)
            else:
                return
        elif direction == self._LEFT:
            if 0 <= col - 1 and matrix[row][col-1] != self._OCCUPIED:
                self._spiralOrderRecursively(matrix, row, col-1, self._LEFT, ans)
            elif 0 <= row - 1 and matrix[row-1][col] != self._OCCUPIED:
                self._spiralOrderRecursively(matrix, row-1, col, self._UP, ans)
            else:
                return
        elif direction == self._UP:
            if 0 <= row - 1 and matrix[row-1][col] != self._OCCUPIED:
                self._spiralOrderRecursively(matrix, row-1, col, self._UP, ans)
            elif col + 1 < len(matrix[0]) and matrix[row][col+1] != self._OCCUPIED:
                self._spiralOrderRecursively(matrix, row, col+1, self._RIGHT, ans)
            else:
                return

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        ans = []
        self._spiralOrderRecursively(matrix, 0, 0, self._RIGHT, ans)
        return ans
