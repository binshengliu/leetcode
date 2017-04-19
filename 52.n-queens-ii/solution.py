class Solution(object):
    def _isSafe(self, board, row, col):
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False

        # top-left
        r, c = row - 1, col - 1
        while 0 <= r and 0 <= c:
            if board[r][c] == 'Q':
                return False
            r, c = r - 1, c - 1

        # top-right
        r, c = row - 1, col + 1
        while 0 <= r and c <= len(board) - 1:
            if board[r][c] == 'Q':
                return False
            r, c = r - 1, c + 1

        # bottom-left
        r, c = row + 1, col - 1
        while r <= len(board) - 1 and 0 <= c:
            if board[r][c] == 'Q':
                return False
            r, c = r + 1, c - 1

        # bottom-right
        r, c = row + 1, col + 1
        while r <= len(board) - 1 and c <= len(board) - 1:
            if board[r][c] == 'Q':
                return False
            r, c = r + 1, c + 1

        return True

    def _formatBoard(self, board):
        return [''.join(board[row]) for row in range(len(board))]

    def _placeQuene(self, board, row, ans):
        for col in range(len(board)):
            if self._isSafe(board, row, col):
                board[row][col] = 'Q'
                if row < len(board) - 1:
                    self._placeQuene(board, row + 1, ans)
                elif row == len(board) - 1:
                    ans.append(self._formatBoard(board))
                else:
                    raise ValueError("row exceeds")
                board[row][col] = '.'

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        self._placeQuene(board, 0, ans)
        return len(ans)
