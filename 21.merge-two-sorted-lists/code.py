# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        ans = ListNode(0)                 #head
        c = ans

        c1 = l1
        c2 = l2
        while c1 != None and c2 != None:
            if c1.val < c2.val:
                c.next = ListNode(c1.val)
                c1 = c1.next
            else:
                c.next = ListNode(c2.val)
                c2 = c2.next
            c = c.next

        while c1 != None:
            c.next = ListNode(c1.val)
            c = c.next
            c1 = c1.next

        while c2 != None:
            c.next = ListNode(c2.val)
            c = c.next
            c2 = c2.next

        return ans.next
