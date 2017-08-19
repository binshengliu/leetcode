class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        transactions = 2
        prices_len = len(prices)
        dp = [[0] * prices_len for i in range(transactions + 1)]

        for i in range(1, transactions+1):
            maxtmp = dp[i-1][0] - prices[0]
            for j in range(1, prices_len):
                dp[i][j] = max(dp[i][j-1], prices[j] + maxtmp)
                maxtmp = max(maxtmp, dp[i-1][j] - prices[j])
            # print(dp[i])

        return dp[-1][-1]

# https://discuss.leetcode.com/topic/4766/a-clean-dp-solution-which-generalizes-to-k-transactions
