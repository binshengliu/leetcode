# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxPathSumHelper(self, root, ans):
        if not root.left and not root.right:
            ans[0] = max(ans[0], root.val)
            return root.val

        left = 0
        if root.left:
            left = self.maxPathSumHelper(root.left, ans)

        right = 0
        if root.right:
            right = self.maxPathSumHelper(root.right, ans)

        # print("left: {}, right: {}, current: {}".format(left, right, root.val))
        max_single_path_throught_self = max(left + root.val, right + root.val, root.val)

        # print("Max single path through {}: {}".format(root.val, max_single_path_throught_self))
        # print("Current max: {}".format(ans[0]))
        ans[0] = max(ans[0], max_single_path_throught_self, left + right + root.val)
        # print("Current max: {}".format(ans[0]))

        # print("return {}".format(max_single_path_throught_self))
        # print("")
        return max_single_path_throught_self

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        ans = [root.val]
        self.maxPathSumHelper(root, ans)
        return ans[0]
