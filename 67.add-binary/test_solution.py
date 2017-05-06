from solution import Solution


def test_1():
    s = Solution()
    ans = s.addBinary('0', '0')
    assert ans == '0'


def test_2():
    s = Solution()
    ans = s.addBinary('1', '1')
    assert ans == '10'


def test_3():
    s = Solution()
    ans = s.addBinary('10', '1')
    assert ans == '11'
