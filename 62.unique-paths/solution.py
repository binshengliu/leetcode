class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        row = m
        col = n

        dp = [[0 for j in range(col)] for i in range(row)]
        dp[0][0] = 1

        for i in range(row):
            for j in range(col):
                if 0 <= i - 1:
                    dp[i][j] += dp[i-1][j]
                if 0 <= j - 1:
                    dp[i][j] += dp[i][j-1]

        ans = dp[row-1][col-1]
        return ans
