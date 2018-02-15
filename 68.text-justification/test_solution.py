from solution import Solution


def test_1():
    s = Solution()
    ans = s.fullJustify(["This", "is", "an", "example", "of", "text",
                         "justification."], 16)
    assert ans == ["This    is    an", "example  of text", "justification.  "]


def test_2():
    s = Solution()
    ans = s.fullJustify(["a", "b", "c", "d", "e"],  1)
    assert ans == ["a", "b", "c", "d", "e"]


def test_3():
    s = Solution()
    ans = s.fullJustify(["Listen", "to", "many, ", "speak", "to", "a",
                         "few."], 6)
    assert ans == ["Listen", "to    ", "many, ", "speak ", "to   a", "few.  "]
