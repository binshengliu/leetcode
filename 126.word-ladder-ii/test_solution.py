from solution import Solution


def test_1():
    s = Solution()
    ans = s.findLadders("hit", "cog",
                        ["hot", "dot", "dog", "lot", "log", "cog"])
    print(ans)
    assert(ans == [['hit', 'hot', 'lot', 'log', 'cog'],
                   ['hit', 'hot', 'dot', 'dog', 'cog']]
           or
           ans == [['hit', 'hot', 'dot', 'dog', 'cog'],
                   ['hit', 'hot', 'lot', 'log', 'cog']])


def test_2():
    s = Solution()
    ans = s.findLadders("hot", "dog", ["hot", "dog"])
    print(ans)
    assert(ans == [])


def test_3():
    s = Solution()
    ans = s.findLadders("hot", "dog",
                        ["hot", "cog", "dog", "tot",
                         "hog", "hop", "pot", "dot"])
    print(ans)
    assert(ans == [["hot", "hog", "dog"], ["hot", "dot", "dog"]]
           or
           ans == [["hot", "dot", "dog"], ["hot", "hog", "dog"]])


def test_4():
    s = Solution()
    ans = s.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    assert(ans == [])


def test_5():
    s = Solution()
    # import pudb.b
    ans = s.findLadders("red", "tax",
                        ["ted", "tex", "red", "tax",
                         "tad", "den", "rex", "pee"])
    print(ans)
