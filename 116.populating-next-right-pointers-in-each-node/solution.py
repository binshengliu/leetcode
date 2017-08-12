# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        # The outer loop visit every level of the tree, and the downp
        # pointer moves along the left branch of the tree. The inner
        # loop visit every node in the same level, and the rightp
        # pointer traverses every node in the same level.
        downp = root
        while downp.left:
            rightp = downp
            while rightp:
                rightp.left.next = rightp.right
                if rightp.next:
                    rightp.right.next = rightp.next.left
                rightp = rightp.next
            downp = downp.left
