class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return 0
        dp = [i for i in range(0, n+1)]
        dp[1] = 0
        for i in range(2, n+1):
            for j in range(2, i):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j]+i//j)
        return dp[n]

s = Solution()
print(s.minSteps(5))
print(s.minSteps(6))
print(s.minSteps(7))
print(s.minSteps(8))
print(s.minSteps(9))
print(s.minSteps(10))
print(s.minSteps(11))
print(s.minSteps(12))

