from solution import Solution


def test_1():
    s = Solution()
    ans = s.generateMatrix(3)
    assert ans == [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5]
    ]
