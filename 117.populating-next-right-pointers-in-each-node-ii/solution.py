# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    def next_connection_for_left_child(self, node):
        if node.right:
            return node.right

        node = node.next
        while node:
            if node.left:
                return node.left

            if node.right:
                return node.right

            node = node.next

        return None

    def next_connection_for_right_child(self, node):
        node = node.next
        while node:
            if node.left:
                return node.left

            if node.right:
                return node.right

            node = node.next

        return None

    def first_node_in_next_level(self, node):
        while node:
            if node.left:
                return node.left

            if node.right:
                return node.right

            node = node.next

        return None

    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        downp = root
        while downp:
            # First round, update the next poitners
            rightp = downp
            while rightp:
                if rightp.left:
                    rightp.left.next = self.next_connection_for_left_child(rightp)

                if rightp.right:
                    rightp.right.next = self.next_connection_for_right_child(rightp)

                rightp = rightp.next

            # Second round, find a path to go down
            downp = self.first_node_in_next_level(downp)
