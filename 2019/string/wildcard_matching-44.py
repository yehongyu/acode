class Solution(object):
    def isMatch_Recuursion(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0: return len(s) == 0
        if p[0]  == '?':
            return len(s)>0 and self.isMatch(s[1:], p[1:])
        elif p[0] == '*':
            return (len(s)==0 and self.isMatch(s, p[1:])) or \
                   (len(s) > 0 and (self.isMatch(s[1:], p) or \
                    self.isMatch(s, p[1:])))
        else:
            return len(s) > 0 and s[0] == p[0] and self.isMatch(s[1:],  p[1:])
        return False

    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        dp = []
        for i in range(m+1):
            dp.append([False] * (n+1))
        dp[0][0] = True
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] | dp[i][j-1] | dp[i-1][j-1]
                elif p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = (s[i-1] == p[j-1]) & dp[i-1][j-1]
        return dp[m][n]




s = Solution()
#print(s.isMatch('aa', 'a'))
#print(s.isMatch('aa', '*'))
#print(s.isMatch('cb', '?a'))
#print(s.isMatch('adceb', '*a*b'))
#print(s.isMatch('aa', 'aa'))
#print(s.isMatch('acdcb', 'a*c?b'))
print(s.isMatch('ho', 'ho**'))
