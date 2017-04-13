from solution import Solution


def test_1():
    s = Solution()
    # import pudb.b
    ans = s.permute([1, 2, 3])
    assert ans == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ]
