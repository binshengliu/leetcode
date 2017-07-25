# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isValidBSTRange(self, root, interval):
        if not root:
            return True

        if interval[0] is not None and root.val <= interval[0]:
            return False

        if interval[1] is not None and root.val >= interval[1]:
            return False

        return self.isValidBSTRange(root.left, (interval[0], root.val)) and \
            self.isValidBSTRange(root.right, (root.val, interval[1]))

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTRange(root, (None, None))
