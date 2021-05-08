class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        cash = 0
        hold = -prices[0]
        for i in range(1, n):
            cash = max(cash, hold+prices[i]-fee)
            hold = max(hold, cash-prices[i])
        return cash

s = Solution()
prices = [1, 3, 2, 8, 4, 9]; fee = 2
print(s.maxProfit(prices, fee))
