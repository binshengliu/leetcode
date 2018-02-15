from solution import Solution
def test_1():
    s = Solution()
    # import pudb.b
    ans = s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    assert len(ans) == len([[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]])
