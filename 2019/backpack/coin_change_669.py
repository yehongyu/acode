import sys
class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def dfs(self, coins, amount, cnt, res):
        if amount == 0:
            res[0] = min(res[0], cnt)
            return
        for coin in coins:
            cur = amount - coin
            if cur >= 0:
                cnt += 1
                self.dfs(coins, cur, cnt, res)
                cnt -= 1

    def coinChange_dfs(self, coins, amount):
        # write your code here
        if amount <= 0: return 0
        res = [sys.maxsize]
        self.dfs(coins, amount, 0, res)
        return res[0] if res[0] < sys.maxsize else -1

    def coinChange_TIMELIMIT(self, coins, amount):
        if amount <= 0: return 0
        n = len(coins)
        if n <= 0: return -1
        tmps = sorted(coins)
        coins = []
        for i in range(n):
            if tmps[i] <= 0: continue
            if len(coins) == 0 or coins[-1] != tmps[i]:
                coins.append(tmps[i])
        n = len(coins)
        if n <= 0: return -1
        if amount % coins[-1] == 0:
            return amount // coins[-1]
        dp = []
        for i in range(n):
            dp.append([sys.maxsize] * (amount+1))
            dp[i][0] = 0
        for j in range(amount+1):
            if j % coins[0] == 0:
                dp[0][j] = j // coins[0]
            print(0, j, dp[0][j])
        for i in range(1, n):
            for j in range(1, amount+1):
                k = 1
                cur = k * coins[i]
                dp[i][j] = min(dp[i][j], dp[i-1][j])
                while cur <= j:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-cur] + k)
                    k += 1
                    cur = k * coins[i]
                if coins[i] <= j:
                    dp[i][j] = min(dp[i][j], dp[i][j-coins[i]] + 1)
                print(i, j, dp[i][j])
        return dp[n-1][amount] if dp[n-1][amount] < sys.maxsize else -1

    def coinChange_TIMELIMMIT2(self, coins, amount):
        if amount <= 0: return 0
        n = len(coins)
        if n <= 0: return -1
        tmps = sorted(coins)
        coins = []
        for i in range(n):
            if tmps[i] <= 0: continue
            if len(coins) == 0 or coins[-1] != tmps[i]:
                coins.append(tmps[i])
        n = len(coins)
        if n <= 0: return -1
        if amount % coins[-1] == 0:
            return amount // coins[-1]
        dp = [0] * (amount+1)
        for j in range(amount+1):
            if j % coins[0] == 0:
                dp[0][j] = j // coins[0]
            print(0, j, dp[0][j])
        for i in range(1, n):
            for j in range(1, amount+1):
                k = 1
                cur = k * coins[i]
                dp[i][j] = min(dp[i][j], dp[i-1][j])
                while cur <= j:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-cur] + k)
                    k += 1
                    cur = k * coins[i]
                if coins[i] <= j:
                    dp[i][j] = min(dp[i][j], dp[i][j-coins[i]] + 1)
                print(i, j, dp[i][j])
        return dp[n-1][amount] if dp[n-1][amount] < sys.maxsize else -1

    def coinChange_DP(self, coins, amount):
        if amount <= 0: return 0
        n = len(coins)
        if n <= 0: return -1
        tmps = sorted(coins)
        coins = []
        for i in range(n):
            if tmps[i] <= 0: continue
            if len(coins) == 0 or coins[-1] != tmps[i]:
                coins.append(tmps[i])
        n = len(coins)
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(1, amount+1):
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] <= amount else -1


    def dfs1(self, coins, res, amount, cnt):
        print(amount, cnt)
        if amount == 0:
            res[0] = min(cnt, res[0])
            return
        for coin in coins:
            if amount - coin >= 0:
                self.dfs1(coins, res, amount-coin, cnt+1)

    def coinChange_DFS(self, coins, amount):
        if amount <= 0: return 0
        n = len(coins)
        if n <= 0: return -1
        res = [amount+1]
        self.dfs1(coins, res, amount, 0)
        return res[0] if res[0] <= amount else -1

    def dfs_mem(self, coins, mem, amount):
        if mem[amount] != sys.maxsize:
            return mem[amount]
        for coin in coins:
            if amount - coin >= 0:
                cnt = self.dfs_mem(coins, mem, amount-coin)
                if cnt < sys.maxsize:
                    mem[amount] = min(mem[amount], cnt + 1)
        return mem[amount]

    def coinChange_DFS_MEM(self, coins, amount):
        if amount <= 0: return 0
        n = len(coins)
        if n <= 0: return -1
        mem = [sys.maxsize] * (amount + 1)
        mem[0] = 0
        self.dfs_mem(coins, mem, amount)
        return mem[amount] if mem[amount] < sys.maxsize else -1

    def dfs_mem_map(self, coins, mem, amount):
        if amount in mem:
            return mem[amount]
        tmp = sys.maxsize
        for coin in coins:
            if amount - coin >= 0:
                cnt = self.dfs_mem_map(coins, mem, amount-coin)
                if cnt < sys.maxsize:
                    tmp = min(tmp, cnt + 1)
        mem[amount] = tmp
        return tmp

    def coinChange_DFS_MEM_MAP(self, coins, amount):
        if amount <= 0: return 0
        n = len(coins)
        if n <= 0: return -1
        mem = {}
        mem[0] = 0
        self.dfs_mem_map(coins, mem, amount)
        return mem[amount] if mem[amount] < sys.maxsize else -1

    def change_DP_2D(self, amount, coins):
        n = len(coins)
        if n <= 0: return 0
        if amount <= 0: return 1
        dp = []
        for i in range(n):
            dp.append([0] * (amount+1))
            dp[i][0] = 1
        for j in range(1, amount+1):
            if j % coins[0] == 0:
                dp[0][j] = 1
        for i in range(1, n):
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j]
                if j - coins[i] >= 0:
                    dp[i][j] += dp[i][j-coins[i]]
        return dp[n-1][amount]

    def change(self, amount, coins):
        n = len(coins)
        if n <= 0: return 0
        if amount <= 0: return 1
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] += dp[j-coin]
        return dp[amount]




s = Solution()
coins = [0,1,1,1,8]
amount = 9
coins = [1,2,5,7]
amount = 11
coins = [2,3,8]
amount = 8
#print(s.coinChange_DFS_MEM_MAP(coins, amount))
print(s.change(amount, coins))
