class Solution:
    """
    @param S: A string
    @param T: A string
    @return: Count the number of distinct subsequences
    """
    def numDistinct(self, S, T):
        # write your code here
        m = len(S)
        n = len(T)
        dp = []
        for i in range(m+1):
            dp.append([0] * (n+1))
        for i in range(m+1):
            dp[i][0] = 1
        for j in range(1, n+1):
            dp[0][j] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if S[i-1] == T[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]

s = Solution()
print(s.numDistinct("rabbbit", "rabbit"))
print(s.numDistinct("rabbit", "rabbit"))
print(s.numDistinct("rabbit", ""))
print(s.numDistinct("", "rabbit"))
