from solution import Solution


def test_1():
    s = Solution()
    # import pudb.b
    ans = s.restoreIpAddresses("25525511135")
    # print(ans)


def test_2():
    s = Solution()
    # import pudb.b
    ans = s.restoreIpAddresses("0000")
    assert ans == ["0.0.0.0"]


def test_3():
    s = Solution()
    # import pudb.b
    ans = s.restoreIpAddresses("000")
    assert ans == []


def test_4():
    s = Solution()
    # import pudb.b
    ans = s.restoreIpAddresses("010010")
    assert ans == ["0.10.0.10", "0.100.1.0"]


def test_5():
    s = Solution()
    # import pudb.b
    ans = s.restoreIpAddresses("101023")
    print(ans)
