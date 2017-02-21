# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        t = head
        i = 0
        d = {}
        while t != None:
            d[i] = t
            i += 1
            t = t.next

        target = i - n
        if target == 0:
            return d[0].next
        else:
            d[target-1].next = d[target].next
            return d[0]
