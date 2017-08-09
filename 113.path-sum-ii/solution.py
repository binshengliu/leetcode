# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        if not root.left and not root.right:
            return [[sum]] if sum == root.val else []

        ans = []

        if root.left:
            sub_ans = self.pathSum(root.left, sum - root.val)
            for one in sub_ans:
                one.insert(0, root.val)
            if sub_ans:
                ans.extend(sub_ans)

        if root.right:
            sub_ans = self.pathSum(root.right, sum - root.val)
            for one in sub_ans:
                one.insert(0, root.val)
            if sub_ans:
                ans.extend(sub_ans)

        return ans
