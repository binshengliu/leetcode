# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = [root]
        ans = []
        level = 0

        while q:
            count = len(q)
            ans.append([])
            for i in range(count):
                node = q[i]
                ans[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            del q[:count]
            level += 1

        return ans
