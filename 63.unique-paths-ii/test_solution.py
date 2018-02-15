from solution import Solution


def test_1():
    s = Solution()
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    ans = s.uniquePathsWithObstacles(grid)
    assert ans == 2


def test_2():
    s = Solution()
    grid = [
        [0, 0],
        [0, 0],
        [0, 0]
    ]
    ans = s.uniquePathsWithObstacles(grid)
    assert ans == 3


def test_3():
    s = Solution()
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    ans = s.uniquePathsWithObstacles(grid)
    assert ans == 0


def test_4():
    s = Solution()
    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    ans = s.uniquePathsWithObstacles(grid)
    assert ans == 0


def test_5():
    s = Solution()
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    ans = s.uniquePathsWithObstacles(grid)
    assert ans == 1


def test_6():
    s = Solution()
    grid = [
        [0, 0, 0]
    ]
    ans = s.uniquePathsWithObstacles(grid)
    assert ans == 1
