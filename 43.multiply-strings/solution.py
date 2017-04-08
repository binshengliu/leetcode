

# https://discuss.leetcode.com/topic/30508/easiest-java-solution-with-graph-explanation
# This is a much more brilliant solution.
class Solution(object):
    def _multiply_single_digit(self, digit1, digit2):
        product = int(digit1) * int(digit2)
        ans = str(product)
        return ans

    def _add(self, num1, num2):
        ans = ''

        reverse_index = 1
        carry = 0
        while reverse_index <= len(num1) and reverse_index <= len(num2):
            digit1 = num1[-reverse_index]
            digit2 = num2[-reverse_index]
            added = int(digit1) + int(digit2) + carry

            carry = 0
            if added >= 10:
                added %= 10
                carry = 1

            ans = str(added) + ans
            reverse_index += 1

        while reverse_index <= len(num1):
            digit1 = num1[-reverse_index]
            added = int(digit1) + carry

            carry = 0
            if added >= 10:
                added %= 10
                carry = 1

            ans = str(added) + ans
            reverse_index += 1

        while reverse_index <= len(num2):
            digit1 = num2[-reverse_index]
            added = int(digit1) + carry

            carry = 0
            if added >= 10:
                added %= 10
                carry = 1

            ans = str(added) + ans
            reverse_index += 1

        if carry == 1:
            ans = '1' + ans

        return ans

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1.count('0') == len(num1) or num2.count('0') == len(num2):
            return '0'

        ans = ''
        for (i, digit1) in enumerate(reversed(num1)):
            if digit1 == '0':
                continue
            elif digit1 == '1':
                sub_ans = num2 + ''.join(['0' for _ in range(i)])
            else:
                sub_ans = ''
                carry = 0
                for (j, digit2) in enumerate(reversed(num2)):
                    product = int(digit1) * int(digit2)
                    product += carry

                    carry = 0
                    if product >= 10:
                        carry = int(product / 10)
                        product %= 10

                    sub_ans = str(product) + sub_ans

                if carry != 0:
                    sub_ans = str(carry) + sub_ans
                sub_ans += ''.join(['0' for _ in range(i)])

            # print('{:>9} * {} = {:>20}'.format(digit1 + ''.join(['0' for _ in range(i)]), num2, sub_ans))
            ans = self._add(ans, sub_ans)

        return ans
