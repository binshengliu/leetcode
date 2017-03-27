# from test import print_board

class Solution(object):
    def isValueValid(self, board, row, col, val):
        '''Test if val is valid'''
        row_vals = board[row]
        if val in row_vals:
            return False

        col_vals = [board[i][col] for i in range(0, 9)]
        if val in col_vals:
            return False

        row_begin = int(row / 3) * 3
        row_end = ((int(row / 3) + 1) * 3)
        col_begin = int(col / 3) * 3
        col_end = ((int(col / 3) + 1) * 3)
        # block_vals = []
        # for i in range(row_begin, row_end):
        #     for j in range(col_begin, col_end):
        #         block_vals.append(board[i][j])

        block_vals = [board[i][j] for i in range(row_begin, row_end) for j in range(col_begin, col_end)]
        if val in block_vals:
            return False

        return True

    def nextPosition(self, row, col):
        '''Find next position'''
        next_row = row
        next_col = (col + 1) % 9
        if next_col == 0:
            next_row = row + 1
        return (next_row, next_col)

    def solveSudokuRec(self, board, row, col):
        # goes beyond the last row
        if row == 9:
            # All done
            return True

        next_row, next_col = self.nextPosition(row, col)

        if board[row][col] == '.':
            # print('\nrow: {}, col: {}'.format(row, col))
            # print_board(board)
            for val in '123456789':
                is_valid = self.isValueValid(board, row, col, val)
                if is_valid:
                    # print('{} is valid at {}, {}'.format(val, row, col))
                    board[row][col] = val

                    # Process next position
                    ans = self.solveSudokuRec(board, next_row, next_col)
                    if ans:
                        return True
                    else:
                        board[row][col] = '.'
                # else:
                #     print('{} is invalid at {}, {}'.format(val, row, col))
        else:
            ans = self.solveSudokuRec(board, next_row, next_col)
            return ans

        # print('unable to continue at row {} col {}'.format(row, col))
        return False


    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solveSudokuRec(board, 0, 0)
        # print_board(board)
