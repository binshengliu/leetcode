# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumNumbersHelper(self, root, parent, ans):
        """
        :type root: TreeNode
        :rtype: (int, int)
        """
        current = parent * 10 + root.val
        if not root.left and not root.right:
            ans[0] += current
            # print("Current: {}, Ans: {}".format(current, ans[0]))
            return

        if root.left:
            self.sumNumbersHelper(root.left, current, ans)

        if root.right:
            self.sumNumbersHelper(root.right, current, ans)

        return

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        ans = [0]
        self.sumNumbersHelper(root, 0, ans)
        return ans[0]
