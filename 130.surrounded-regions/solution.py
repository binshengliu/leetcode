class Solution(object):
    def try_mark(self, board, row, col):
        if board[row][col] != 'O':
            return

        q = [(row, col)]
        while q:
            (row, col) = q.pop(0)
            if board[row][col] != 'O':
                continue

            board[row][col] = '.'
            if row > 0:
                q.append((row-1, col))

            if row < len(board) - 1:
                q.append((row+1, col))

            if col > 0:
                q.append((row, col-1))

            if col < len(board[0]) - 1:
                q.append((row, col+1))

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])
        for col in range(cols):
            self.try_mark(board, 0, col)
            self.try_mark(board, rows-1, col)

        for row in range(rows):
            self.try_mark(board, row, 0)
            self.try_mark(board, row, cols-1)

        for (row_index, row) in enumerate(board):
            for (col_index, elem) in enumerate(row):
                if elem == 'O':
                    board[row_index][col_index] = 'X'
                if elem == '.':
                    board[row_index][col_index] = 'O'
