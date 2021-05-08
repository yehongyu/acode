class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
        if n <= 0 or amount < 0: return -1
        import sys
        dp = [-1] * (amount+1)
        dp[0] = 0
        coins = sorted(coins)
        ## no zero, no duplicate
        for j in range(1, amount+1):
            for i in range(0, n):
                if j-coins[i] >= 0 and dp[j-coins[i]] != -1:
                    if dp[j] == -1:
                        dp[j] = dp[j-coins[i]]+1
                    else:
                        dp[j] = min(dp[j], dp[j-coins[i]]+1)
        return dp[amount]

s = Solution()
coins = [1, 2, 5]; amount = 11
coins = [2, 5]; amount = 3
coins = [1, 2147483647]; amount = 2
coins = [186,419,83,408]
amount = 6249
print(s.coinChange(coins, amount))
