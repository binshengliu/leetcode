# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        min_depth = 99999999999999
        if root.left:
            left_min_depth = 1 + self.minDepth(root.left)
            min_depth = min(min_depth, left_min_depth)

        if root.right:
            right_min_depth = 1 + self.minDepth(root.right)
            min_depth = min(min_depth, right_min_depth)

        return min_depth
