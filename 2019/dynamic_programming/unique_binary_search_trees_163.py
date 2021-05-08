class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def numTrees(self, n):
        # write your code here
        if n <= 1: return 1
        if n == 2: return 2
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            for k in range(1, i+1):
                dp[i] += dp[k-1] * dp[i-k]
        return dp[n]

s = Solution()
print(s.numTrees(3))
print(s.numTrees(4))
print(s.numTrees(5))
