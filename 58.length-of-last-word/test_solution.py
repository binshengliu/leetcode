from solution import Solution


def test_1():
    s = Solution()
    ans = s.lengthOfLastWord("abc")
    assert ans == 3


def test_2():
    s = Solution()
    ans = s.lengthOfLastWord("abc defg")
    assert ans == 4


def test_3():
    s = Solution()
    ans = s.lengthOfLastWord("  abc   defgh      ")
    assert ans == 5


def test_4():
    s = Solution()
    ans = s.lengthOfLastWord("      ")
    assert ans == 0
