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
    # import pudb.b
    ans = s.partition(list_to_linked_list([1, 1]), 2)
    assert linked_list_to_list(ans) == [1, 1]


def test_2():
    s = Solution()
    # import pudb.b
    ans = s.partition(list_to_linked_list([1, 4, 3, 2, 5, 2]), 3)
    assert linked_list_to_list(ans) == [1, 2, 2, 4, 3, 5]
