from solution import Solution


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "val: {}, next: {}".format(self.val,
                                          self.next.val
                                          if self.next
                                          else "None")


def test_1():
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    ans = s.rotateRight(node1, 2)
    assert ans.val == 4


def test_2():
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    ans = s.rotateRight(node1, 5)
    assert ans.val == 1
