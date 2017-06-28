from solution import Solution


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{}, {}".format(self.val, self.next)


def list_to_linked_list(val):
    if not val:
        return None

    ret = ListNode(0)
    current = ret
    for c in val:
        current.next = ListNode(c)
        current = current.next
    return ret.next


def linked_list_to_list(linked):
    l = []
    c = linked
    while c:
        l.append(c.val)
        c = c.next
    return l


def print_linked_list(msg, l):
    print(msg)
    while l:
        print(l.val, end=' ', flush=True)
        l = l.next
    print('\n')


def test_1():
    s = Solution()
    l = [1, 2, 3, 4, 5]
    ans = s.reverseBetween(list_to_linked_list(l), 2, 4)
    assert linked_list_to_list(ans) == [1, 4, 3, 2, 5]


def test_2():
    s = Solution()
    l = [1, 2, 3, 4, 5]
    ans = s.reverseBetween(list_to_linked_list(l), 1, 3)
    assert linked_list_to_list(ans) == [3, 2, 1, 4, 5]


def test_3():
    s = Solution()
    l = [1, 2, 3, 4, 5]
    ans = s.reverseBetween(list_to_linked_list(l), 1, 5)
    assert linked_list_to_list(ans) == [5, 4, 3, 2, 1]


def test_4():
    s = Solution()
    l = [1, 2, 3, 4, 5]
    ans = s.reverseBetween(list_to_linked_list(l), 1, 1)
    assert linked_list_to_list(ans) == [1, 2, 3, 4, 5]


def test_5():
    s = Solution()
    l = [1, 2, 3, 4, 5]
    ans = s.reverseBetween(list_to_linked_list(l), 4, 5)
    assert linked_list_to_list(ans) == [1, 2, 3, 5, 4]


def test_6():
    s = Solution()
    l = [1, 2, 3, 4, 5]
    ans = s.reverseBetween(list_to_linked_list(l), 5, 5)
    assert linked_list_to_list(ans) == [1, 2, 3, 4, 5]


def test_7():
    s = Solution()
    l = [1, 2, 3, 4, 5]
    ans = s.reverseBetween(list_to_linked_list(l), 5, 4)
    assert linked_list_to_list(ans) == [1, 2, 3, 4, 5]
