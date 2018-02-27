from solution import Solution


def test_1():
    s = Solution()
    nums = [1, 3, 5, 7]
    result = s.rob(nums)
    assert (result == 10)
