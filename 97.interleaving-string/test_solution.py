from solution import Solution


def test_1():
    s = Solution()
    ans = s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
    assert ans


def test_2():
    s = Solution()
    ans = s.isInterleave("aabcc", "dbbca", "aadbbbaccc")
    assert not ans


def test_3():
    s = Solution()
    ans = s.isInterleave("", "", "")
    assert ans


def test_4():
    s = Solution()
    ans = s.isInterleave("a", "b", "a")
    assert not ans


def test_5():
    s = Solution()
    # import pudb.b
    ans = s.isInterleave("aabc", "abad", "aabadabc")
    assert ans
