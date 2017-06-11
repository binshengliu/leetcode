# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "val: {}, next: {}".format(self.val, self.next)


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None

        small_head = ListNode(0)
        small_head.next = head
        small_cursor = small_head
        prev = small_head
        current = head

        while current:
            if current.val >= x:
                prev = current
                current = current.next
                continue

            if small_cursor.next == current:
                small_cursor = small_cursor.next
                prev = current
                current = current.next
                continue

            next = current.next
            prev.next = current.next
            current.next = small_cursor.next
            small_cursor.next = current
            current = next
            small_cursor = small_cursor.next

        return small_head.next
