from code import Solution
def test_1():
    s = Solution()
    # import pudb.b
    ans = s.combinationSum([2, 3, 6, 7], 7)
    assert len(ans) == len([[7], [2, 2, 3]])

def test_2():
    s = Solution()
    # import pudb.b
    ans = s.combinationSum([5, 10, 8, 4, 3, 12, 9], 27)
    assert len(ans) == len([[3,3,3,3,3,3,3,3,3],[3,3,3,3,3,3,4,5],[3,3,3,3,3,3,9],[3,3,3,3,3,4,4,4],[3,3,3,3,3,4,8],[3,3,3,3,3,12],[3,3,3,3,5,5,5],[3,3,3,3,5,10],[3,3,3,4,4,5,5],[3,3,3,4,4,10],[3,3,3,4,5,9],[3,3,3,5,5,8],[3,3,3,8,10],[3,3,3,9,9],[3,3,4,4,4,4,5],[3,3,4,4,4,9],[3,3,4,4,5,8],[3,3,4,5,12],[3,3,4,8,9],[3,3,5,8,8],[3,3,9,12],[3,4,4,4,4,4,4],[3,4,4,4,4,8],[3,4,4,4,12],[3,4,4,8,8],[3,4,5,5,5,5],[3,4,5,5,10],[3,4,8,12],[3,4,10,10],[3,5,5,5,9],[3,5,9,10],[3,8,8,8],[3,12,12],[4,4,4,5,5,5],[4,4,4,5,10],[4,4,5,5,9],[4,4,9,10],[4,5,5,5,8],[4,5,8,10],[4,5,9,9],[5,5,5,12],[5,5,8,9],[5,10,12],[8,9,10],[9,9,9]])
