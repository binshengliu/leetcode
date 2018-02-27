from solution import Solution


def test_1():
    s = Solution()
    nums = [1, 3, 5, 7]
    result = s.rob(nums)
    assert (result == 10)


def test_2():
    s = Solution()
    nums = [1]
    result = s.rob(nums)
    assert (result == 1)


def test_3():
    s = Solution()
    nums = [1, 2]
    result = s.rob(nums)
    assert (result == 2)


def test_4():
    s = Solution()
    nums = [1, 2, 3]
    result = s.rob(nums)
    assert (result == 3)
