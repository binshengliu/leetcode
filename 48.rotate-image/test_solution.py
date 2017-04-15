from solution import Solution

def test_1():
    s = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    s.rotate(matrix)

    assert matrix == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]]
