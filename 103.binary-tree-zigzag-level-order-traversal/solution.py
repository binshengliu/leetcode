# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = [root]
        ans = []
        level = 0
        left_to_right = True

        while q:
            count = len(q)
            ans.append([])

            for i in (range(count) if left_to_right else range(count-1, -1, -1)):
                node = q[i]
                ans[level].append(node.val)

            for i in range(count):
                node = q[i]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            left_to_right = not left_to_right
            del q[:count]
            level += 1

        return ans
