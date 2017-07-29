# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrderRecursively(self, root, level, ans):
        if not root:
            return

        if len(ans) <= level:
            ans.append([])

        ans[level].append(root.val)
        self.levelOrderRecursively(root.left, level + 1, ans)
        self.levelOrderRecursively(root.right, level + 1, ans)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        self.levelOrderRecursively(root, 0, ans)
        return ans
