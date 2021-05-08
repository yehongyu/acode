class Solution:
    """
    @param cost: costs of all cards
    @param damage: damage of all cards
    @param totalMoney: total of money
    @param totalDamage: the damage you need to inflict
    @return: Determine if you can win the game
    """
    def cardGame(self, cost, damage, totalMoney, totalDamage):
        # Write your code here
        n = len(cost)
        if n <= 0 or totalMoney <= 0: return False
        dp = [0] * (totalMoney + 1)
        for i in range(n):
            for j in range(totalMoney, cost[i]-1, -1):
                dp[j] = max(dp[j], dp[j-cost[i]] + damage[i])
        if dp[totalMoney] >= totalDamage:
            return True
        return False

s = Solution()
cost = [1,2,3,4,5]
damage = [1,2,3,4,5]
totalMoney = 10
totalDamage = 10
cost = [1,2]
damage = [3,4]
totalMoney = 10
totalDamage = 10
print(s.cardGame(cost, damage, totalMoney, totalDamage))

