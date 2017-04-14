from solution import Solution


def test_1():
    s = Solution()
    # import pudb.b
    ans = s.permuteUnique([1, 1, 2])
    assert ans == [
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]
    ]
