from solution import Solution


def test_1():
    s = Solution()
    ans = s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
    assert ans


def test_2():
    s = Solution()
    ans = s.isInterleave("aabcc", "dbbca", "aadbbbaccc")
    assert not ans
