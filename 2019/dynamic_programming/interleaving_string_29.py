class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        m = len(s1)
        n = len(s2)
        k = len(s3)
        if m + n != k:
            return False
        dp = []
        for i in range(m+1):
            dp.append([False] * (n+1))
        dp[0][0] = True
        for i in range(1, m+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]
        for j in range(1, n+1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = dp[0][j-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s3[i-1+j]:
                    dp[i][j] |= dp[i-1][j]
                if s2[j-1] == s3[i-1+j]:
                    dp[i][j] |= dp[i][j-1]
        return dp[m][n]

s = Solution()
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(s.isInterleave("", "", "1"))
print(s.isInterleave("aabcc", "dbbca", "aadbbbaccc"))



