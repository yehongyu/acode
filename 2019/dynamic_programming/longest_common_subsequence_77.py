class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        m = len(A)
        n = len(B)
        dp = []
        for i in range(m+1):
            dp.append([0] * (n+1))
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
                else:
                    dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]

s = Solution()
print(s.longestCommonSubsequence("ABCD", "EACB"))
