from solution import Solution


def test_1():
    s = Solution()
    # import pudb.b
    ans = s.trap([1, 0, 1])
    assert ans == 1


def test_2():
    s = Solution()
    # import pudb.b
    ans = s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    assert ans == 6


def test_empty():
    s = Solution()
    # import pudb.b
    ans = s.trap([])
    assert ans == 0


def test_3():
    s = Solution()
    # import pudb.b
    ans = s.trap([5, 4, 1, 2])
    assert ans == 1
