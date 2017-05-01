class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        dp = [[0 for j in range(col)] for i in range(row)]
        if obstacleGrid[row-1][col-1] == 0:
            dp[row-1][col-1] = 1

        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue

                if i < row - 1:
                    dp[i][j] += dp[i+1][j]

                if j < col - 1:
                    dp[i][j] += dp[i][j+1]

        ans = dp[0][0]
        return ans
