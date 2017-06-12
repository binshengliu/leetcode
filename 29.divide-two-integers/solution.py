class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 2 ** 31 - 1

        if dividend == -(2 ** 31) and divisor == -1:
            return 2 ** 31 - 1

        sign1 = 1
        if dividend < 0:
            dividend = -dividend
            sign1 = -1

        sign2 = 1
        if divisor < 0:
            divisor = -divisor
            sign2 = -1

        ans = 0
        while dividend >= divisor:
            tmp = divisor
            shift = 0
            while dividend >= (tmp << 1):
                tmp <<= 1
                shift += 1

            if shift != 0:
                dividend -= (divisor << shift)
                ans += 1 << shift
            else:
                dividend -= divisor
                ans += 1

        if sign1 != sign2:
            ans = -ans

        return ans
