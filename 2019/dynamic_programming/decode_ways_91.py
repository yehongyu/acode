class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0 or s[0]=='0': return 0
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i-2 >= 0 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
            print(i, dp[i])
        return dp[n]

s = Solution()
print(s.numDecodings('226'))
