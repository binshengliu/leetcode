# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    prev = None
    first = None
    second = None

    def recover(self, root):
        if not root:
            return

        self.recover(root.left)

        if not self.first and self.prev and self.prev.val >= root.val:
            self.first = self.prev

        if self.first and self.prev and self.prev.val >= root.val:
            self.second = root

        self.prev = root

        self.recover(root.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.recover(root)
        self.first.val, self.second.val = self.second.val, self.first.val

# https://discuss.leetcode.com/topic/3988/no-fancy-algorithm-just-simple-and-powerful-in-order-traversal
