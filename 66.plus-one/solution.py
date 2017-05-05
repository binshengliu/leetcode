class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for (i, digit) in reversed(list(enumerate(digits))):
            digit += carry
            if digit == 10:
                carry = 1
                digits[i] = 0
            else:
                digits[i] = digit
                return digits

        if carry == 1:
            digits.insert(0, 1)

        return digits
