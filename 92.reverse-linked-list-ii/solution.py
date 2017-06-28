# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{}, {}".format(self.val, self.next)


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # Index given by the problem starts from 1
        index = 1
        fake_head = ListNode(0)
        fake_head.next = head
        prev_m = fake_head
        prev = fake_head
        current = head

        # After execution, prev points the element at position m-1,
        # and current points to the element at position m
        while current and index < m:
            prev = current
            current = current.next
            index += 1

        # Go beyond the list
        if not current:
            return fake_head.next

        # After execution, prev_m points to m-1, prev points to m,
        # current points m+1
        prev_m = prev
        prev = current
        current = current.next
        index += 1

        while current and index <= n:
            prev.next = current.next
            current.next = prev_m.next
            prev_m.next = current
            current = prev.next

            index += 1

        return fake_head.next
