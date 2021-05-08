class Solution(object):
    def isMatch_Recurison(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        print('s=', s, 'p=', p)
        if len(p) == 0: return len(s) == 0
        if len(p) > 1 and p[1] == '*':
            if self.isMatch(s, p[2:]): return True
            if (len(s) > 0 and (s[0] == p[0] or p[0] == '.')):
                return self.isMatch(s[1:], p)
            return False
        else:
            return len(s) > 0 and (s[0]==p[0] or p[0]=='.') and self.isMatch(s[1:], p[1:])


    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        dp = []
        for i in range(m+1): dp.append([False] * (n+1))
        dp[0][0] = True
        for j in range(2, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] != '*':
                    if p[j-1] == '.' or p[j-1] == s[i-1]:
                        dp[i][j] = dp[i-1][j-1]
                else:
                    if j-2 >= 0:
                        dp[i][j] |= dp[i][j-2]
                        if (p[j-2] == s[i-1] or p[j-2] ==  '.'):
                            dp[i][j] |= dp[i-1][j]
        return dp[m][n]


s = Solution()
print(s.isMatch('aa', 'a*'))

