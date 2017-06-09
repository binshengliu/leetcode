from solution import Solution


def test_1():
    s = Solution()
    # import pudb.b
    ans = s.largestRectangleArea([2, 1, 5, 6, 2, 3])
    assert ans == 10


def test_2():
    s = Solution()
    # import pudb.b
    ans = s.largestRectangleArea([2, 1, 5, 6, 2, 2, 2, 2, 23])
    assert ans == 23
