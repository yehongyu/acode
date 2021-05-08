class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == -1: return 0
        dp = []
        for i in  range(m):
            dp.append([0] * n)
        dp[0][0] = grid[0][0]
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == -1: dp[i][j] = 0
                else:
                    dp[i][j] = grid[i][j]
                    if i-1>=0 and j-1>=0:
                        dp[i][j] += max(dp[i-1][j], dp[i][j-1])
                    elif i-1>=0:
                        dp[i][j] += dp[i-1][j]
                    elif j-1>=0:
                        dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]

s = Solution()
grid = [[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
print(s.cherryPickup(grid))

