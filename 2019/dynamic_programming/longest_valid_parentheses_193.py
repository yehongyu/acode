class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def longestValidParentheses_old(self, s):
        # write your code here
        n = len(s)
        dp = [0] * (n+1)
        res = 0
        for i in range(1, n+1):
            if s[i-1] == '(':
                dp[i] = 0
            elif s[i-1] == ')':
                idx = i-dp[i-1]-2
                if idx >= 0 and s[idx] == '(':
                    dp[i] = dp[i-1] + 2 + dp[idx]
            res = max(res, dp[i])
        return res

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n<= 1: return 0
        dp = [0] * (n+1)
        res = 0
        for i in range(1,n+1):
            if s[i-1] == '(': continue
            start = i-dp[i-1]-2
            if start >= 0 and s[start] == '(':
                dp[i] = dp[start] + i - start
                res = max(dp[i], res)
        return res


s = Solution()
print(s.longestValidParentheses('(()'))
print(s.longestValidParentheses(')()())'))
print(s.longestValidParentheses('(()(())'))




