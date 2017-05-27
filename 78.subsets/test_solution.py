from solution import Solution


def test_empty():
    s = Solution()
    ans = s.subsets([])
    assert ans == [[]]


def test_1():
    s = Solution()
    # import pudb.b
    ans = s.subsets([1, 2])
    print(ans)


def test_2():
    s = Solution()
    ans = s.subsets([1, 2, 3])
    print(ans)
