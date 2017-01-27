def compare(a, b):
    """
    a and b are both string representations of positive numbers
    """
    while a and a[0] == '0':
        a = a[1:]
    while b and b[0] == '0':
        b = b[1:]

    if len(a) > len(b):
        return 1
    elif len(a) < len(b):
        return -1

    for n1, n2 in zip(a, b):
        if n1 > n2:
            return 1
        elif n1 < n2:
            return -1

    return 0

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxint = str(2 ** 31 - 1)
        minint = str(2 ** 31)

        positive = (x >= 0)
        s = str(abs(x))
        s = s[::-1]

        if positive and (compare(s, maxint) == 1):
            return 0
        elif (not positive) and (compare(s, minint) == 1):
            return 0

        ret = int(s)
        if not positive:
            ret = -ret
        return ret
