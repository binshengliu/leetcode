class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minp = 0
        for i in range(len(prices)):
            if prices[i] < prices[minp]:
                minp = i

            if prices[i] - prices[minp] > profit:
                profit = prices[i] - prices[minp]

        return profit
