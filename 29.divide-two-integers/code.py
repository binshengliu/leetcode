import sys

class Solution(object):
    def simple_divide(self, dividend, divisor):
        ans = 0
        tmp = divisor
        while tmp <= dividend:
            tmp += divisor
            ans += 1
        return (ans, dividend - (tmp - divisor))

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

        str_dividend = str(dividend)
        str_ans = ''
        tmp_dividend = ''
        for i in str_dividend:
            tmp_dividend += i

            # print('tmp dividend: {}, divisor: {}'.format(tmp_dividend, divisor))

            (tmp_ans, remain) = self.simple_divide(int(tmp_dividend), divisor)
            str_ans += str(tmp_ans)

            tmp_dividend = ''
            if remain != 0:
                tmp_dividend = str(remain)

        ans = int(str_ans)
        if sign1 != sign2:
            ans = -ans

        # Special condition: handle int overflow
        if ans > (2 ** 31 - 1) or ans < -(2 ** 31):
            return (2 ** 31 - 1)

        return ans
