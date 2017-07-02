# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversalRecursively(self, current, result):
        if not current:
            return

        self.inorderTraversalRecursively(current.left, result)
        result.append(current.val)
        self.inorderTraversalRecursively(current.right, result)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.inorderTraversalRecursively(root, ans)
        return ans
