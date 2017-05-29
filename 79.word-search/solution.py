class Solution(object):
    def is_invalid_pos(self, board, used, row_index, col_index):
        if row_index < 0 or row_index >= len(board) \
           or col_index < 0 or col_index >= len(board[0]):
            return False

        if used[row_index][col_index]:
            return False

        return True

    def exist_with_bitmap(self, board, used, row_index, col_index, word):
        if not word:
            return True

        if not self.is_invalid_pos(board, used, row_index, col_index):
            return False

        if used[row_index][col_index]:
            return False

        if board[row_index][col_index] != word[0]:
            return False

        used[row_index][col_index] = True
        next_pos = [(row_index-1, col_index), (row_index+1, col_index),
                    (row_index, col_index-1), (row_index, col_index+1)]
        for (next_row, next_col) in next_pos:
            ans = self.exist_with_bitmap(board, used, next_row, next_col,
                                         word[1:])
            if ans:
                break

        used[row_index][col_index] = False
        return ans

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True

        row = len(board)
        col = len(board[0])
        used = [[False for c in range(col)] for r in range(row)]

        for row_index in range(row):
            for col_index in range(col):
                ans = self.exist_with_bitmap(board, used,
                                             row_index, col_index, word)
                if ans:
                    return True

        return False
