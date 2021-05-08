class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        n = len(s)
        m = len(p)
        dp = []
        for i in range(n+1):
            dp.append([False] * (m+1))
        dp[0][0] = True
        for i in range(1, m+1):
            if p[i-1] == '*':
                dp[0][i] = i-2>=0 and dp[0][i-2]
        print(dp[0])
        for i in range(1, n+1):
            for j in range(1, m+1):
                if p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if j-2>=0 and p[j-2] == '.':
                        dp[i][j] = dp[i][j-2]
                    if j-2>= 0:
                        if p[j-2] == '.' or s[i-1] == p[j-2]:
                            dp[i][j] |= dp[i-1][j]
                        else:
                            dp[i][j] |= dp[i][j-2]
                else:
                    dp[i][j] = s[i-1] == p[j-1] and dp[i-1][j-1]
                print(i, j, dp[i][j])
        return dp[n][m]

s = Solution()

#print(s.isMatch("aab", "c*a*b"))
print(s.isMatch("aab", "*"))
#print(s.isMatch("aabce", "c*a*b.e"))

