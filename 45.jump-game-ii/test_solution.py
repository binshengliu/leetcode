from solution import Solution


def test_1():
    s = Solution()
    a = [2, 3, 1, 1, 4]
    # import pudb.b
    ans = s.jump(a)
    assert ans == 2


def test_2():
    s = Solution()
    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]
    # import pudb.b
    ans = s.jump(a)
    assert ans == 2
