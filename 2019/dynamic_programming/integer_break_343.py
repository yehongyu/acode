class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        if n == 1: return 1
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, int(i/2)+1):
                cur = max(dp[j], j) * max(dp[i-j], i-j)
                dp[i] = max(dp[i], cur)
        return dp[n]

s = Solution()
print(s.integerBreak(2))
print(s.integerBreak(10))

