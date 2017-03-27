import unittest
import code

def print_board(board):
    for (i, line) in enumerate(board):
        if i != 0 and i % 3 == 0:
            print('-----------', flush=True)
        for (j, char) in enumerate(line):
            if j != 0 and j % 3 == 0:
                print('|', end='')
            print(char, end='')
        print('', flush=True)

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = code.Solution()
        board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
                 ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
                 ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
                 ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
                 ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
                 ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
                 ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
                 ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
                 ['.', '.', '.', '.', '8', '.', '.', '7', '9']]

        print_board(board)
        s.solveSudoku(board)
        print('')
        print_board(board)

if __name__ == '__main__':
    unittest.main()
