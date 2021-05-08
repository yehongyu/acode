class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        m = len(costs)
        if m < 1:
            return 0
        n = len(costs[0])
        dp = []
        for i in range(m):
            dp.append([0] * n)
        dp[0] = costs[0]
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = costs[i][j] + min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])
        return min(dp[m-1])

    def firstWillWin(self, values):
        m = len(values)
        if m <= 2: return True
        dp = [0] * (m+2)
        dp[m-1] = values[m-1]
        dp[m-2] = values[m-1] + values[m-2]
        for i in range(m-3, -1, -1):
            dp[i] = max(values[i] + min(dp[i+2], dp[i+3]),
                        values[i]+values[i+1] + min(dp[i+3], dp[i+4]))
        return dp[0] > sum(values) - dp[0]




s = Solution()
costs = [[14,2,11],[11,14,5],[14,3,10]]
costs = [[1,2,3],[1,4,6]]
#print(s.minCost(costs))

print(s.firstWillWin([1, 2, 2]))
print(s.firstWillWin([1, 2, 4]))

