from code import Solution


def test_1():
    s = Solution()
    # import pudb.b
    ans = s.firstMissingPositive([9, 3, 4, 4, 1, 2])
    assert ans == 5


def test_2():
    s = Solution()
    # import pudb.b
    ans = s.firstMissingPositive([3, 4, -1, 1])
    assert ans == 2


def test_empty():
    s = Solution()
    ans = s.firstMissingPositive([])
    assert ans == 1
