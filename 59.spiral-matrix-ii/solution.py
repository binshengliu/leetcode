class Solution(object):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

    def _canGoRight(self, matrix, n, row, col):
        return col < n - 1 and matrix[row][col+1] == 0

    def _canGoDown(self, matrix, n, row, col):
        return row < n - 1 and matrix[row+1][col] == 0

    def _canGoLeft(self, matrix, n, row, col):
        return 0 < col and matrix[row][col-1] == 0

    def _canGoUp(self, matrix, n, row, col):
        return 0 < row and matrix[row-1][col] == 0

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        row = 0
        col = 0
        direction = Solution.RIGHT
        for val in range(n ** 2):
            matrix[row][col] = val + 1
            if direction == Solution.RIGHT:
                if self._canGoRight(matrix, n, row, col):
                    col += 1
                elif self._canGoDown(matrix, n, row, col):
                    row += 1
                    direction = Solution.DOWN
                else:
                    assert val == (n**2 - 1)
                continue
            elif direction == Solution.DOWN:
                if self._canGoDown(matrix, n, row, col):
                    row += 1
                elif self._canGoLeft(matrix, n, row, col):
                    col -= 1
                    direction = Solution.LEFT
                else:
                    assert val == (n**2 - 1)
                continue
            elif direction == Solution.LEFT:
                if self._canGoLeft(matrix, n, row, col):
                    col -= 1
                elif self._canGoUp(matrix, n, row, col):
                    row -= 1
                    direction = Solution.UP
                else:
                    assert val == (n**2 - 1)
                continue
            elif direction == Solution.UP:
                if self._canGoUp(matrix, n, row, col):
                    row -= 1
                elif self._canGoRight(matrix, n, row, col):
                    col += 1
                    direction = Solution.RIGHT
                else:
                    assert val == (n**2 - 1)
                continue
            else:
                raise ValueError("Unknown direction.")

        return matrix
