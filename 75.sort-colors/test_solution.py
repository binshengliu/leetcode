from solution import Solution


def test_1():
    s = Solution()
    nums = [0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 0]
    # import pudb.b
    s.sortColors(nums)
    assert nums == [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]


def test_2():
    s = Solution()
    nums = [0, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 2, 0]
    # import pudb.b
    s.sortColors(nums)
    assert nums == [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
