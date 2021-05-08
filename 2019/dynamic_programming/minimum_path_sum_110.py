class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        dp = []
        for i in range(m):
            dp.append([0] * n)
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]

s = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
grid = [[1,3,2]]
print(s.minPathSum(grid))
