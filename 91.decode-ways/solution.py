class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, len(s)+1):
            # if current digit is "0", the previous one must be "1" or
            # "2". Or else, this is an invalid input.
            if s[i-1] == '0' and (s[i-2] != '1' and s[i-2] != '2'):
                return 0

            two_digit = int(s[i-2:i])
            if two_digit == 10 or two_digit == 20:
                dp[i] = dp[i-2]
            elif two_digit <= 9:
                dp[i] = dp[i-1]
            elif two_digit <= 26:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]

        return dp[len(s)]
