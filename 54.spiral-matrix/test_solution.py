from solution import Solution


def test_1():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s = Solution()
    ans = s.spiralOrder(matrix)
    assert ans == [1, 2, 3, 6, 9, 8, 7, 4, 5]
