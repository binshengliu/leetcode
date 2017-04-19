from solution import Solution


def test_1():
    s = Solution()
    ans = s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert ans == 6
