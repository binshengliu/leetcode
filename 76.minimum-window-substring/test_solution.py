from solution import Solution


def test_1():
    s = Solution()
    ans = s.minWindow('ADOBECODEBANC', 'ABC')
    assert ans == 'BANC'


def test_2():
    s = Solution()
    ans = s.minWindow('A', '')
    assert ans == ''
