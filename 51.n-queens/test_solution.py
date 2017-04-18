from solution import Solution


def test_1():
    s = Solution()
    ans = s.solveNQueens(4)
    assert ans == [
        [".Q..",  # Solution 1
         "...Q",
         "Q...",
         "..Q."],

        ["..Q.",  # Solution 2
         "Q...",
         "...Q",
         ".Q.."]]


def test_2():
    s = Solution()
    ans = s.solveNQueens(8)
    print()
    for one_ans in ans:
        for row in one_ans:
            print(row)
        print()
