'''https://leetcode.com/problems/valid-sudoku/#/description'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        blocks = [{} for i in range(9)]

        for (i, row) in enumerate(board):
            for (j, number) in enumerate(row):
                if number in '0123456789':
                    if number in rows[i]:
                        return False
                    rows[i][number] = 1

                    if number in cols[j]:
                        return False
                    cols[j][number] = 1

                    block = int(i / 3) * 3 + int(j / 3)
                    if number in blocks[block]:
                        return False
                    blocks[block][number] = 1
                elif number == '.':
                    continue
                else:
                    return False

        return True
