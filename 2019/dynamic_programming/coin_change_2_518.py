class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n = len(coins)
        if n <= 0 or amount < 0: return 0
        coins = sorted(coins)
        dp = [0] * (amount+1)
        dp[0] = 1
        for j in range(n):
            for i in range(1, amount+1):
                if i-coins[j]>=0 and dp[i-coins[j]] >0:
                    dp[i] += dp[i-coins[j]]
            print(i, dp[i])
        return dp[amount]

s = Solution()
print(s.change(5, [1,2,5]))
