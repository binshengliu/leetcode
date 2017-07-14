from solution import Solution


def test_1():
    s = Solution()
    ans = s.generateTrees(1)
    print(ans)


def test_2():
    s = Solution()
    # import pudb.b
    ans = s.generateTrees(3)
    for one in ans:
        print(one)
    # print(len(ans))
