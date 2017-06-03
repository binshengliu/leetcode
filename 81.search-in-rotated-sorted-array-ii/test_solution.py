from solution import Solution


def test_1():
    s = Solution()
    ans = s.search([4, 5, 6, 7, 0, 1, 2], 5)
    assert ans


def test_2():
    s = Solution()
    ans = s.search([4, 5, 6, 7, 0, 1, 2], 8)
    assert not ans


def test_3():
    s = Solution()
    # import pudb.b
    ans = s.search([3, 1], 2)
    assert not ans


def test_4():
    s = Solution()
    # import pudb.b
    ans = s.search([1, 1, 3, 1], 3)
    assert ans


def test_5():
    s = Solution()
    # import pudb.b
    ans = s.search([3, 1], 1)
    assert ans
