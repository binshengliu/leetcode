from solution import Solution


def test_1():
    s = Solution()
    grid = [[1, 1, 1]]
    ans = s.minPathSum(grid)
    assert ans == 3


def test_2():
    s = Solution()
    grid = [[1, 1, 1],
            [1, 0, 2]]
    ans = s.minPathSum(grid)
    assert ans == 4
