from solution import Solution


def float_equal(f1, f2):
    if abs(f1 - f2) < 0.00001:
        return True
    return False


def test_1():
    s = Solution()
    ans = s.myPow(8.88023, 3)
    assert float_equal(ans, 700.28148)


def test_2():
    s = Solution()
    ans = s.myPow(0.00001, 2147483647)
    print(ans)


def test_3():
    s = Solution()
    ans = s.myPow(4, 23)
    assert float_equal(ans, pow(4, 23))


def test_4():
    s = Solution()
    ans = s.myPow(34.00515, -3)
    assert float_equal(ans, 0.00003)
