class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        sub_ans = self.grayCode(n - 1)
        added = 2 ** (n - 1)
        ans = sub_ans + [i + added for i in reversed(sub_ans)]
        return ans
