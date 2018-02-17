from solution import Solution


def test_1():
    s = Solution()
    assert(s.minCut("aab") == 1)


def test_2():
    s = Solution()
    assert(s.minCut("aabb") == 1)


def test_3():
    s = Solution()
    assert(s.minCut("aaba") == 1)


def test_4():
    s = Solution()
    assert(s.minCut("cbaabcdefedcba") == 3)
