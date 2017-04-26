from solution import Solution


def test_1():
    s = Solution()
    ans = s.getPermutation(3, 3)
    assert ans == '213'
