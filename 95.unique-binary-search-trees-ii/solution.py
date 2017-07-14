# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.val, self.left, self.right)


class Solution(object):
    def generateSubTrees(self, start, end):
        if start > end:
            return []

        ans = []
        for i in range(start, end + 1):
            left_sub_ans = self.generateSubTrees(start, i - 1)
            right_sub_ans = self.generateSubTrees(i + 1, end)
            if not left_sub_ans:
                left_sub_ans = [None]
            if not right_sub_ans:
                right_sub_ans = [None]

            for left_tree in left_sub_ans:
                for right_tree in right_sub_ans:
                    root = TreeNode(i)
                    root.left = left_tree
                    root.right = right_tree
                    ans.append(root)

        return ans

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []

        ans = self.generateSubTrees(1, n)
        return ans
