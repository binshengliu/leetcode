from solution import Solution
def test_1():
    s = Solution()
    # import pudb.b
    ans = s.countAndSay(1)
    assert ans == '1'

def test_3():
    s = Solution()
    # import pudb.b
    ans = s.countAndSay(3)
    assert ans == '21'

def test_5():
    s = Solution()
    # import pudb.b
    ans = s.countAndSay(5)
    assert ans == '111221'

def test_10():
    s = Solution()
    # import pudb.b
    ans = s.countAndSay(10)
    assert ans == '13211311123113112211'
