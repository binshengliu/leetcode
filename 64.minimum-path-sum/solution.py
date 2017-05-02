class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])

        dp = [[0 for j in range(col)] for i in range(row)]

        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if i < row - 1 and j < col - 1:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + grid[i][j]
                elif i < row - 1:
                    dp[i][j] = dp[i+1][j] + grid[i][j]
                elif j < col - 1:
                    dp[i][j] = dp[i][j+1] + grid[i][j]
                else:
                    dp[i][j] = grid[i][j]

        ans = dp[0][0]
        return ans
