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
    ans = s.insert([Interval(1, 3), Interval(6, 9)], Interval(2, 5))
    assert ans == [Interval(1, 5), Interval(6, 9)]


def test_2():
    s = Solution()
    # import pudb.b
    ans = s.insert([Interval(1, 2), Interval(3, 5), Interval(6, 7),
                    Interval(8, 10), Interval(12, 16)], Interval(4, 9))
    assert ans == [Interval(1, 2), Interval(3, 10), Interval(12, 16)]


def test_3():
    s = Solution()
    ans = s.insert([], Interval(5, 7))
    assert ans == [Interval(5, 7)]


def test_4():
    s = Solution()
    ans = s.insert([Interval(1, 5)], Interval(2, 3))
    assert ans == [Interval(1, 5)]
