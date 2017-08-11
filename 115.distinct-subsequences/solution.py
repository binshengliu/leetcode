class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        len_s = len(s)
        len_t = len(t)
        dp = [[0] * (len_s + 1) for i in range(len_t + 1)]
        for j in range(len_s + 1):
            dp[0][j] = 1

        for i in range(1, len_t + 1):
            for j in range(1, len_s + 1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[-1][-1]

# https://discuss.leetcode.com/topic/9488/easy-to-understand-dp-in-java
