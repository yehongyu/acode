class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        # write your code here
        m = len(A)
        if m <= 0: return 0
        if m == 1: return A[0]
        if m == 2: return A[0] + A[2]
        dp = []
        for i in range(m):
            dp.append([0] * m)
        for step in range(1, m):
            for i in range(0, m-step):
                j = i + step
                tmpsum = sum(A[i:j+1])
                dp[i][j] = dp[i][j-1] + tmpsum
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k-1] + dp[k][j] + tmpsum)
                print(i, j, dp[i][j])
        return dp[0][m-1]

s = Solution()
#print(s.stoneGame([3, 4, 3]))
#print(s.stoneGame([4, 1, 1, 4]))
print(s.stoneGame([1, 1, 1, 1]))
