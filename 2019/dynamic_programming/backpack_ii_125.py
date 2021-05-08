class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        n = len(V)
        if n == 0:
            return 0
        dp = []
        for i in range(n+1):
            dp.append([0] * (m+1))
        for i in range(1, n+1):
            for j in range(1, m+1):
                if j-A[i-1] >= 0:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i-1]]+V[i-1])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][m]

s = Solution()
print(s.backPackII(10, [2, 3, 5, 7], [1, 5, 2, 4]))
