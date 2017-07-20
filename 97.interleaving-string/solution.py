class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if len3 != (len1 + len2):
            return False

        dp = [[False for j in range(len2 + 1)] for i in range(len1 + 1)]
        dp[0][0] = True

        for i in range(1, len1 + 1):
            dp[i][0] = False
            if s1[i-1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]

        for j in range(1, len2 + 1):
            dp[0][j] = False
            if s2[j-1] == s3[j-1]:
                dp[0][j] = dp[0][j-1]

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # dp[i][j] is true whichever condition is true.
                # if s1[i-1] == s3[i+j-1]:
                #     dp[i][j] = dp[i-1][j]
                # if s2[j-1] == s3[i+j-1]:
                #     dp[i][j] = dp[i][j-1]
                dp[i][j] = (s1[i-1] == s3[i+j-1] and dp[i-1][j]) or \
                           (s2[j-1] == s3[i+j-1] and dp[i][j-1])

        return dp[len1][len2]

# https://leetcode.com/articles/interleaving-strings/#approach-3-using-2-d-dynamic-programming-accepted
