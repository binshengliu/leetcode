class Solution(object):
    def _countNumber(self, number):
        """Count the single number
        """
        str_n = str(number) + '\0'
        count = 0
        ans = ''
        for (i, c) in enumerate(str_n):
            if i == 0:
                count = 1
            elif c == str_n[i-1]:
                count += 1
            elif c != str_n[i-1]:
                ans += str(count) + str_n[i-1]
                count = 1

        return ans

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = '1'
        for i in range(1, n):
            ans = self._countNumber(ans)

        return ans
