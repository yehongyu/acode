class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1: return 0
        dp = [0] * n
        res = 0
        for i in range(1, n):
            cur = prices[i] - prices[i-1]
            dp[i] = max(dp[i-1] + cur, cur, 0)
            for j in range(0, i-2):
                dp[i] = max(dp[i], dp[j] + cur)
            print(i, dp[i])
            res = max(res, dp[i])
        return res

s = Solution()
prices = [1,2,3,0,2]
prices = [6,1,3,2,4,7]
prices = [6,1,6,4,3,0,2]
print(s.maxProfit(prices))
