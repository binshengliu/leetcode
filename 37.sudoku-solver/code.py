# from test import print_board


class Solution(object):
    def __init__(self):
        self._row_vals = [set() for _ in range(0, 9)]
        self._col_vals = [set() for _ in range(0, 9)]
        self._block_vals = [set() for _ in range(0, 9)]

    def __toBlockId(self, row, col):
        block_id = int(row / 3) * 3 + int(col / 3)
        return block_id

    def __toRowCol(self, block_id):
        row_begin = int(block_id / 3) * 3
        col_begin = int(block_id % 3) * 3
        return (row_begin, col_begin)

    def __addValue(self, row, col, val):
        block_id = self.__toBlockId(row, col)
        self._row_vals[row].add(val)
        self._col_vals[col].add(val)
        self._block_vals[block_id].add(val)

    def __removeValue(self, row, col, val):
        block_id = self.__toBlockId(row, col)
        self._row_vals[row].remove(val)
        self._col_vals[col].remove(val)
        self._block_vals[block_id].remove(val)

    def __isValueValid(self, row, col, val):
        '''Test if val is valid'''
        if val in self._row_vals[row]:
            return False

        if val in self._col_vals[col]:
            return False

        block_id = self.__toBlockId(row, col)
        if val in self._block_vals[block_id]:
            return False

        return True

    def __nextPosition(self, row, col):
        '''Find next position'''
        next_row = row
        next_col = (col + 1) % 9
        if next_col == 0:
            next_row = row + 1
        return (next_row, next_col)

    def __solveSudokuRec(self, board, row, col):
        # goes beyond the last row
        if row == 9:
            # All done
            return True

        next_row, next_col = self.__nextPosition(row, col)

        if board[row][col] == '.':
            # print('\nrow: {}, col: {}'.format(row, col))
            # print_board(board)
            for val in '123456789':
                is_valid = self.__isValueValid(row, col, val)
                if is_valid:
                    # print('{} is valid at {}, {}'.format(val, row, col))
                    board[row][col] = val
                    self.__addValue(row, col, val)

                    # Process next position
                    ans = self.__solveSudokuRec(board, next_row, next_col)
                    if ans:
                        return True
                    else:
                        board[row][col] = '.'
                        self.__removeValue(row, col, val)
                # else:
                #     print('{} is invalid at {}, {}'.format(val, row, col))
        else:
            ans = self.__solveSudokuRec(board, next_row, next_col)
            return ans

        # print('unable to continue at row {} col {}'.format(row, col))
        return False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for row in range(0, 9):
            self._row_vals[row] = set(
                [val for val in board[row] if val != '.'])

        for col in range(0, 9):
            self._col_vals[col] = set([
                board[row][col] for row in range(0, 9)
                if board[row][col] != '.'
            ])

        for block in range(0, 9):
            (row_begin, col_begin) = self.__toRowCol(block)
            row_end = row_begin + 3
            col_end = col_begin + 3
            self._block_vals[block] = set([
                board[row][col]
                for row in range(row_begin, row_end)
                for col in range(col_begin, col_end) if board[row][col] != '.'
            ])

        self.__solveSudokuRec(board, 0, 0)
        # print_board(board)
