class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        n = len(s)
        if n <= 1: return n
        dp = []
        for i in range(n):
            dp.append([0] * n)
            dp[i][i] = 1
        print(n)
        for step in range(2, n+1):
            for i in range(0, n-step+1):
                j = i + step - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                print(i,j, dp[i][j])
        return dp[0][n-1]


    def generateParenthesis(self, n):
        if n == 0: return []
        if n == 1: return ['()']
        curs = self.generateParenthesis(n-1)
        res = []
        for cur in curs:
            tmp = '(' + cur + ')'
            res.append(tmp)
            tmp = cur + '()'
            res.append(tmp)
        return res


s = Solution()
print(s.longestPalindromeSubseq('bbbbb'))

