import sys

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return sys.maxsize

        sign1 = 1
        if dividend < 0:
            dividend = -dividend
            sign1 = -1

        sign2 = 1
        if divisor < 0:
            divisor = -divisor
            sign2 = -1

        ans = 0
        tmp = divisor
        while tmp <= dividend:
            tmp += divisor
            ans += 1

        if sign1 != sign2:
            ans = -ans

        return ans
