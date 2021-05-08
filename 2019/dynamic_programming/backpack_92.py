class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        if n <= 0:
            return 0
        dp = []
        for i in range(n+1):
            dp.append([False] * (m+1))
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, n+1):
            for j in range(1, m+1):
                if j-A[i-1] >= 0:
                    dp[i][j] = dp[i-1][j-A[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        for j in range(m, -1, -1):
            if dp[n][j]: return j

s = Solution()
print(s.backPack(10, [20,15,15,15,15,15,15,15,15,15,15,15,15,15,15,7,2,15,15,15,15]))
