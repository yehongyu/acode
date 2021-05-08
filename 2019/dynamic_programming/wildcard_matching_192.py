class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here
        m = len(s)
        n = len(p)
        dp = []
        for i in range(m+1):
            dp.append([False] * (n+1))
        dp[0][0] = True
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
        print(dp[0])
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] | dp[i][j-1] | dp[i-1][j-1]
                elif p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if p[j-1] == s[i-1]:
                        dp[i][j] = dp[i-1][j-1]
                print(i, j, s[i-1], p[j-1], dp[i][j])
        return dp[m][n]

s = Solution()
print(s.isMatch("aa", "a*"))
print(s.isMatch("aa", "*a"))
print(s.isMatch("ab", "?*"))


