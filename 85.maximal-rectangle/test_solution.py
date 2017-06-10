from solution import Solution


def test_1():
    s = Solution()
    # import pudb.b
    ans = s.maximalRectangle(["10100", "10111", "11111", "10010"])
    assert ans == 6


def test_2():
    s = Solution()
    # import pudb.b
    ans = s.maximalRectangle(["0001000",
                              "0011100",
                              "0111110"])
    assert ans == 6


def test_3():
    s = Solution()
    # import pudb.b
    ans = s.maximalRectangle(["10111",
                              "01010",
                              "11011",
                              "11011",
                              "01111"])
    assert ans == 6
