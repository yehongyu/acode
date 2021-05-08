class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        if n == 1: return 1
        dp = [i for i in range(n+1)]
        for i in range(0, n+1):
            j = 1
            while i + j*j <= n:
                cur = i + j * j
                print(i, j*j, cur)
                dp[cur] = min(dp[cur], dp[i]+1)
                j += 1
        print(dp)
        return dp[n]
s = Solution()
print(s.numSquares(7))
