# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        prev_slow = None
        slow = head
        fast = head.next

        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        if prev_slow:
            prev_slow.next = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head if head != slow else None)
        root.right = self.sortedListToBST(slow.next)

        return root
