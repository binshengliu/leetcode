class Solution(object):

    def gen(self, l, s, n, m):
        if n == 0 and m == 0:
            l.append(s)
            return

        if n > 0:
            self.gen(l, s + '(', n - 1, m + 1)

        if m > 0:
            self.gen(l, s + ')', n, m - 1)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        self.gen(l, '', n, 0)
        return l
