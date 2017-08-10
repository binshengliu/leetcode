# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def flatten_helper(self, root):
        if not root:
            return None

        left_leaf = self.flatten_helper(root.left)
        right_leaf = self.flatten_helper(root.right)

        # print("Root {}".format(root.val))
        # print("Left root {}, left leaf {}".format(root.left.val if root.left else None, left_leaf.val if left_leaf else None))
        # print("Right root {}, right leaf {}\n".format(root.right.val if root.right else None, right_leaf.val if right_leaf else None))

        if left_leaf:
            left_leaf.right = root.right

        if root.left:
            root.right = root.left

        root.left = None

        # print("Root {}".format(root.val))
        # print("Left {}".format(root.left.val if root.left else None))
        # print("Right {}\n".format(root.right.val if root.right else None))

        if right_leaf:
            return right_leaf
        elif left_leaf:
            return left_leaf
        else:
            return root

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.flatten_helper(root)
