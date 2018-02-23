from solution import Solution


def test_1():
    nums = [2, 3, -2, 4]
    s = Solution()
    assert(s.maxProduct(nums) == 6)


def test_2():
    nums = [0, 2]
    s = Solution()
    assert(s.maxProduct(nums) == 2)


def test_3():
    nums = [2, -5, -2, -4, 3]
    s = Solution()
    assert(s.maxProduct(nums) == 24)


def test_4():
    nums = [-2, 3, -4]
    s = Solution()
    assert(s.maxProduct(nums) == 24)
