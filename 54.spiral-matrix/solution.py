class Solution(object):
    GO_LEFT = 0
    GO_RIGHT = 1
    GO_DOWN = 2
    GO_UP = 3
    VISITED = '.'

    def _canGoRight(self, matrix, row, col):
        return (col + 1 < len(matrix[0]) and matrix[row][col+1] != self.VISITED)

    def _canGoDown(self, matrix, row, col):
        return (row + 1 < len(matrix) and matrix[row+1][col] != self.VISITED)

    def _canGoLeft(self, matrix, row, col):
        return (0 <= col - 1 and matrix[row][col-1] != self.VISITED)

    def _canGoUp(self, matrix, row, col):
        return (0 <= row - 1 and matrix[row-1][col] != self.VISITED)

    def _spiralOrderRecursively(self, matrix, row, col, direction, ans):
        """row and col must be valid"""
        ans.append(matrix[row][col])
        matrix[row][col] = self.VISITED
        if direction == self.GO_RIGHT:
            if self._canGoRight(matrix, row, col):
                self._spiralOrderRecursively(matrix, row, col+1, self.GO_RIGHT, ans)
            elif self._canGoDown(matrix, row, col):
                self._spiralOrderRecursively(matrix, row+1, col, self.GO_DOWN, ans)
            else:
                return
        elif direction == self.GO_DOWN:
            if self._canGoDown(matrix, row, col):
                self._spiralOrderRecursively(matrix, row+1, col, self.GO_DOWN, ans)
            elif self._canGoLeft(matrix, row, col):
                self._spiralOrderRecursively(matrix, row, col-1, self.GO_LEFT, ans)
            else:
                return
        elif direction == self.GO_LEFT:
            if self._canGoLeft(matrix, row, col):
                self._spiralOrderRecursively(matrix, row, col-1, self.GO_LEFT, ans)
            elif self._canGoUp(matrix, row, col):
                self._spiralOrderRecursively(matrix, row-1, col, self.GO_UP, ans)
            else:
                return
        elif direction == self.GO_UP:
            if self._canGoUp(matrix, row, col):
                self._spiralOrderRecursively(matrix, row-1, col, self.GO_UP, ans)
            elif self._canGoRight(matrix, row, col):
                self._spiralOrderRecursively(matrix, row, col+1, self.GO_RIGHT, ans)
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
        self._spiralOrderRecursively(matrix, 0, 0, self.GO_RIGHT, ans)
        return ans
