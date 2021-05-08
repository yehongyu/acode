class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        n = len(A)
        acc = [0]
        dp = []
        for i in range(K+1):
            dp.append([0] * (n+1))
        for i in range(n):
            acc.append(acc[-1]+A[i])
            dp[1][i+1] = acc[-1] / (i+1)
        for k in range(2, K+1):
            for i in range(k, n+1):
                for j in range(k-1, i):
                    dp[k][i] = max(dp[k][i], dp[k-1][j]+(acc[i]-acc[j])/(i-j))
        return dp[K][n]

s = Solution()
A = [9,1,2,3,9]
K = 3
A=[1,2,3,4,5,6,7]
K=4
print(s.largestSumOfAverages(A, K))


