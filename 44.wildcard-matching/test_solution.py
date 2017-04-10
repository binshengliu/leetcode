from solution import Solution

def test_1():
    s = Solution()

    # import pudb.b
    ans = s.isMatch('aa', 'a')
    assert not ans

    ans = s.isMatch('aa', 'aa')
    assert ans

    ans = s.isMatch('aaa', 'aa')
    assert not ans

    ans = s.isMatch('aa', '*')
    assert ans

    ans = s.isMatch('aa', 'a*')
    assert ans

    ans = s.isMatch('ab', '?*')
    assert ans

    ans = s.isMatch('aab', 'c*a*b')
    assert not ans
