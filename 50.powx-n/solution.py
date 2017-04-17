class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n

        if n == 0:
            return 1

        if n == 1:
            return x

        ans = x
        exp = 1
        while exp * 2 <= n:
            ans *= ans
            exp *= 2

        if exp < n:
            ans *= self.myPow(x, n - exp)

        return ans
