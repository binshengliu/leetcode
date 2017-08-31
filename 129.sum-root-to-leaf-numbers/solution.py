# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumNumbersHelper(self, root):
        """
        :type root: TreeNode
        :rtype: (int, int)
        """
        if not root.left and not root.right:
            return [(root.val, 0)]

        # print("current: {}".format(root.val))
        ans = []
        if root.left:
            sub_ans = self.sumNumbersHelper(root.left)
            ans.extend([(left_sum + root.val * (10 ** (left_depth + 1)), left_depth + 1)
                        for (left_sum, left_depth) in sub_ans])
            # print("left: {}, left depth: {}".format(left_sum, left_depth))
            # print("total left: {}".format(sum))

        if root.right:
            sub_ans = self.sumNumbersHelper(root.right)
            ans.extend([(right_sum + root.val * (10 ** (right_depth + 1)), right_depth + 1)
                        for (right_sum, right_depth) in sub_ans])
            # print("right: {}".format(right_sum))

        return ans

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        ans = self.sumNumbersHelper(root)
        # print("{}".format(ans))
        sum_num = sum([branch[0] for branch in ans])
        return sum_num
