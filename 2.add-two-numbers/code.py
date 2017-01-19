# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        ret = None
        cur = None

        while l1 != None or l2 != None:
            if None == cur:
                cur = ListNode(0)
            else:
                cur.next = ListNode(0)
                cur = cur.next

            if None == ret:
                ret = cur

            if None != l1:
                cur.val = cur.val + l1.val
                l1 = l1.next

            if None != l2:
                cur.val = cur.val + l2.val
                l2 = l2.next

            cur.val = cur.val + carry
            carry = 0
            if cur.val >= 10:
                carry = cur.val / 10
                cur.val = cur.val % 10

        if 0 != carry:
            cur.next = ListNode(carry)

        return ret
