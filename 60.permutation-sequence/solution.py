import math


class Solution(object):
    def genFactorial(self, n):
        self._factorial = {}
        val = 1
        for i in range(1, n+1):
            val *= i
            self._factorial[i] = val

    # digit_index starts from 1, starting from most significant digit
    def getPermutationRecursively(self, n, l, k, digit_index):
        if n == digit_index:
            return str(l[0])

        candidates_per_digit = self._factorial[n - digit_index]

        # The float conversion is a workaround for leetcode
        current_index = int(math.ceil(float(k) / candidates_per_digit)) - 1

        # list indes starts from 0, so minus 1
        current_value = l[current_index]

        l.remove(current_value)
        sub_ans = self.getPermutationRecursively(n, l,
                                                 k % candidates_per_digit,
                                                 digit_index+1)

        ans = str(current_value) + sub_ans
        return ans

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.genFactorial(n)
        l = [i for i in range(1, n+1)]

        ans = self.getPermutationRecursively(n, l, k, 1)

        return ans
