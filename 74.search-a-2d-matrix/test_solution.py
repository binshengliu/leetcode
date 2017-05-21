from solution import Solution


def test_1():
    s = Solution()
    ans = s.searchMatrix([[1,   3,  5,  7],
                          [10, 11, 16, 20],
                          [23, 30, 34, 50]],
                         17)
    assert not ans
