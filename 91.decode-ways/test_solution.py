from solution import Solution


def test_1():
    s = Solution()
    ans = s.numDecodings('1')
    assert ans == 1


def test_2():
    s = Solution()
    ans = s.numDecodings('12')
    assert ans == 2


def test_3():
    s = Solution()
    ans = s.numDecodings('123456')
    assert ans == 3


def test_4():
    s = Solution()
    ans = s.numDecodings("1212121212")
    assert ans == 89


def test_5():
    s = Solution()
    ans = s.numDecodings("30")
    assert ans == 0


def test_6():
    s = Solution()
    ans = s.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")
    assert ans == 589824
