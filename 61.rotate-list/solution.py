# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or k == 0:
            return head

        list_count = 0
        node = head
        while node:
            list_count += 1
            node = node.next

        k %= list_count
        if k == 0:
            return head

        # Three nodes that need to be modified
        new_head = None
        new_last = head
        old_last = None
        node = head
        passed = 0
        while node.next:
            node = node.next
            if passed < k:
                passed += 1
                continue
            new_last = new_last.next

        new_head = new_last.next
        new_last.next = None
        old_last = node
        old_last.next = head

        return new_head
