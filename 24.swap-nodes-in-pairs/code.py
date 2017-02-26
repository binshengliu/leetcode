# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head

        p = head
        if p != None and p.next != None:
            hn = head.next
            hnn = head.next.next

            head.next = hnn
            hn.next = head
            head = hn

        p = head.next
        while p != None and p.next != None and p.next.next != None:
            pn = p.next
            pnn = p.next.next

            p.next = pnn
            pn.next = pnn.next
            pnn.next = pn
            p = pn

        return head
