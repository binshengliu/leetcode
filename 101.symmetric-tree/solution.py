# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtreeSymmetric(self, left, right):
        if not left and not right:
            return True

        if left and right and left.val == right.val:
            return self.isSubtreeSymmetric(left.left, right.right) and \
                self.isSubtreeSymmetric(left.right, right.left)

        return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.isSubtreeSymmetric(root.left, root.right)
