# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def checkHeight(self, root):
        """
        get the balance status and height of the subtree
        """
        if not root:
            return (True, 0)

        left_height = 0
        right_height = 0

        if root.left:
            left_balanced, left_height = self.checkHeight(root.left)
            if not left_balanced:
                return (False, 0)
            left_height += 1

        if root.right:
            right_balanced, right_height = self.checkHeight(root.right)
            if not right_balanced:
                return (False, 0)
            right_height += 1

        balanced = True
        if abs(left_height - right_height) > 1:
            balanced = False

        return (balanced, max(left_height, right_height))

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        (balanced, height) = self.checkHeight(root)

        return balanced
