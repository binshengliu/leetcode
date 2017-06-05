# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        ans = head
        cursor = head
        current_node = head.next if head else None
        cursor.next = None
        while current_node:
            next_node = current_node.next
            if cursor.val != current_node.val:
                cursor.next = current_node
                cursor = current_node
                cursor.next = None

            current_node = next_node

        return ans
