class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        num = x
        digits = 0
        while num != 0:
            num = int(num / 10)
            digits += 1

        num = x
        while num != 0:
            lsn = num % 10
            msn = int(num / (10 ** (digits - 1)))
            if lsn != msn:
                return False

            num = num - msn * (10 ** (digits - 1))
            num = int(num / 10)
            digits -= 2
            # print('num: {}, digits: {}'.format(num, digits))

        return True
