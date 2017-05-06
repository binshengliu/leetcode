class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []

        carry = 0
        a_index = len(a) - 1
        b_index = len(b) - 1
        while 0 <= a_index and 0 <= b_index:
            bit = int(a[a_index]) + int(b[b_index]) + carry

            carry = 1 if bit >= 2 else 0
            bit %= 2

            result.insert(0, str(bit))

            a_index -= 1
            b_index -= 1

        while 0 <= a_index:
            bit = int(a[a_index]) + carry
            carry = 1 if bit >= 2 else 0

            bit %= 2
            result.insert(0, str(bit))

            a_index -= 1

        while 0 <= b_index:
            bit = int(b[b_index]) + carry

            carry = 1 if bit >= 2 else 0
            bit %= 2

            result.insert(0, str(bit))
            b_index -= 1

        if carry == 1:
            result.insert(0, '1')

        ans = ''.join(result)
        return ans
