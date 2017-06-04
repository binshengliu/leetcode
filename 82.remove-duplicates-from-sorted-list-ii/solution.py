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
        ans = None
        cursor = None
        prev_node = None
        current_node = head
        next_node = current_node.next if current_node and current_node.next \
            else None
        # import pudb.b
        while current_node:
            if (not prev_node or prev_node.val != current_node.val) \
               and (not next_node or current_node.val != next_node.val):
                current_node.next = None
                if not ans:
                    ans = current_node
                    cursor = ans
                else:
                    cursor.next = current_node
                    cursor = cursor.next

            prev_node = current_node
            current_node = next_node
            next_node = next_node.next if next_node else None

        return ans
