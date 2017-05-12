from solution import Solution


def test_1():
    s = Solution()
    ans = s.simplifyPath('/a/')
    assert ans == '/a'


def test_2():
    s = Solution()
    ans = s.simplifyPath('/a/./b/../../c/')
    assert ans == '/c'


def test_3():
    s = Solution()
    ans = s.simplifyPath('//a//./b/../../c/')
    assert ans == '/c'


def test_4():
    s = Solution()
    ans = s.simplifyPath('/../a//./b/../../c/')
    assert ans == '/c'


def test_5():
    s = Solution()
    ans = s.simplifyPath('/../')
    assert ans == '/'
