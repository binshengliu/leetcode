from solution import Solution


def test_1():
    s = Solution()
    ans = s.minDistance("abc", "def")
    assert ans == 3


def test_2():
    s = Solution()
    ans = s.minDistance("abcdef", "acdf")
    assert ans == 2


def test_3():
    s = Solution()
    ans = s.minDistance("", "a")
    assert ans == 1
