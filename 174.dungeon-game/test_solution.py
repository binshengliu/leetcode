from solution import Solution


def test_1():
    dungeon = [[0]]
    s = Solution()
    result = s.calculateMinimumHP(dungeon)
    assert (result == 1)


def test_2():
    dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    s = Solution()
    result = s.calculateMinimumHP(dungeon)
    assert (result == 7)


def test_3():
    dungeon = [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]
    s = Solution()
    result = s.calculateMinimumHP(dungeon)
    assert (result == 3)


def test_4():
    dungeon = [[1, -4, 5, -99], [2, -2, -2, -1]]
    s = Solution()
    result = s.calculateMinimumHP(dungeon)
    assert (result == 3)
