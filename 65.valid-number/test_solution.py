from solution import Solution


def test_1():
    s = Solution()
    ans = s.isNumber("a")
    assert not ans


def test_2():
    s = Solution()
    ans = s.isNumber("1 3")
    assert not ans


def test_3():
    s = Solution()
    # import pudb.b
    ans = s.isNumber("3.1e1")
    assert ans


def test_4():
    s = Solution()
    ans = s.isNumber("3.1e")
    assert not ans


def test_5():
    s = Solution()
    ans = s.isNumber("0")
    assert ans

    ans = s.isNumber(" 0.1 ")
    assert ans

    ans = s.isNumber("abc")
    assert not ans

    ans = s.isNumber("1 a")
    assert not ans

    ans = s.isNumber("2e10")
    assert ans


def test_6():
    s = Solution()
    ans = s.isNumber(".")
    assert not ans


def test_7():
    s = Solution()
    ans = s.isNumber("3e3.1")
    assert not ans


def test_8():
    s = Solution()
    ans = s.isNumber("-e58")
    assert not ans


def test_9():
    s = Solution()
    # import pudb.b
    ans = s.isNumber(" 005047e+6")
    assert ans


def test_10():
    s = Solution()
    # import pudb.b
    ans = s.isNumber("+.8")
    assert ans


def test_11():
    s = Solution()
    # import pudb.b
    ans = s.isNumber(" -.")
    assert not ans


def test_12():
    s = Solution()
    ans = s.isNumber("46.e3")
    assert ans
