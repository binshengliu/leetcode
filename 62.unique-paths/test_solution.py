from solution import Solution


def test_1():
    s = Solution()
    ans = s.uniquePaths(2, 2)
    assert ans == 2


def test_2():
    s = Solution()
    ans = s.uniquePaths(3, 2)
    assert ans == 3


def test_3():
    s = Solution()
    ans = s.uniquePaths(3, 7)
    assert ans == 28
