# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Inspired by
# https://discuss.leetcode.com/topic/7031/simple-java-solution-in-one-pass

# Use a slow and fast point with distance of n + 1. When fast reaches end of
# the list, remove next of slow. Otherwise, slow itself needs to be removed,
# and it must be head.
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        slow = head
        gap = 0
        while fast != None:
            fast = fast.next
            if gap == n + 1:
                slow = slow.next
            else:
                gap += 1

        # print(slow.val)
        # print(slow.next)
        # print("slow: {}, head: {}".format(slow, head))
        if gap == n + 1:
            slow.next = slow.next.next
        else:
            head = head.next
        return head
