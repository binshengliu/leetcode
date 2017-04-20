from solution import Solution


def test_1():
    s = Solution()
    ans = s.canJump([2, 3, 1, 1, 4])
    assert ans


def test_2():
    s = Solution()
    ans = s.canJump([3, 2, 1, 0, 4])
    assert not ans


def test_3():
    s = Solution()
    ans = s.canJump([0, 2])
    assert not ans
