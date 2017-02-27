# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        # print('head: {}, k: {}'.format(head, k))
        if head == None:
            return head

        if k == 1 or k == 0:
            return head

        c = head
        for i in range(k):
            if c == None:       # there are no k elements left
                return head
            c = c.next

        first = head
        prev = head
        c = head.next
        for i in range(k - 1):
            # preserve next
            n = c.next

            # reverse
            # print('reverse {} and {}'.format(prev.val, c.val))
            c.next = prev

            # advance
            prev = c
            c = n

        # now, first becomes last in this session
        # first.next = None
        # print_linked_list('', prev)
        # print('----------------------')

        first.next = self.reverseKGroup(c, k)
        return prev
