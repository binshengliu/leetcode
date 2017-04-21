from solution import Solution


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, rhs):
        return self.start == rhs.start and self.end == rhs.end

    def __repr__(self):
        return "({}, {})".format(self.start, self.end)


def test_1():
    s = Solution()
    ans = s.merge([Interval(1, 3), Interval(2, 6), Interval(8, 10),
                   Interval(15, 18)])
    assert ans == [Interval(1, 6), Interval(8, 10), Interval(15, 18)]


def test_2():
    s = Solution()
    ans = s.merge([Interval(1, 4), Interval(2, 5)])
    assert ans == [Interval(1, 5)]


def test_3():
    s = Solution()
    ans = s.merge([Interval(2, 3), Interval(4, 5), Interval(6, 7),
                   Interval(8, 9), Interval(1, 10)])
    assert ans == [Interval(1, 10)]
