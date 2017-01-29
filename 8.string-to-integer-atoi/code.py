import string

# As if this is completed in C

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = 1

        num = 0

        str = str.strip()

        if len(str) <= 0:
            return 0

        if str[0] == '+':
            sign = 1
            str = str[1:]
        elif str[0] == '-':
            sign = -1
            str = str[1:]

        for c in str:
            if c in string.digits:
                num = num * 10 + int(c)
            else:
                break

        num = num * sign

        if num > 2 ** 31 - 1:
            num = 2 ** 31 - 1
        elif num < -2 ** 31:
            num = -2 ** 31

        return num
