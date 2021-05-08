class Solution:
    """
    @param n: The number of 'A'
    @return: the minimum number of steps to get n 'A'
    """
    def minSteps_Recursion(self, n):
        # Write your code here
        if n <= 1: return 0
        res = n
        for i in range(n-1, 1, -1):
            if n % i == 0:
                res = min(res, self.minSteps(n//i) + i)
        return res

    def minSteps(self, n):
        if n <= 1: return 0
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = i
            for j in range(i-1, 1, -1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i//j)
        return dp[n]

    def maxA_Recursion(self, N):
        if N <= 0: return 0
        res = N
        for i in range(1, N-2):
            res = max(res, self.maxA(i) * (N-i-1))
        return res

    def maxA(self, N):
        if N <= 0: return 0
        dp = [0] * (N+1)
        for i in range(1, N+1):
            dp[i] = i
            for j in range(1, i-2):
                dp[i] = max(dp[i], dp[j] * (i-j-1))
        return dp[N]

s = Solution()
print(s.maxA(7))

#print(s.minSteps(6))