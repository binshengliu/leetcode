from solution import Solution


def test_1():
    s = Solution()
    ans = s.getPermutation(3, 3)
    assert ans == '213'


def test_2():
    s = Solution()
    ans = s.getPermutation(2, 1)
    assert ans == '12'


def test_3():
    s = Solution()
    ans = s.getPermutation(3, 1)
    assert ans == '123'
