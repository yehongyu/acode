class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, A, k, target):
        # write your code here
        n = len(A)
        if n <= 0:
            return 0
        dp = []
        for i in range(n+1):
            tmp = []
            for j in range(k+1):
                tmp.append([0] * (target+1))
            dp.append(tmp)
        for i in range(n+1):
            dp[i][0][0] = 1
        for i in range(1, n+1):
            for j in range(1, k+1):
                for t in range(1, target+1):
                    if t-A[i-1] >= 0:
                        dp[i][j][t] = dp[i-1][j][t] + dp[i-1][j-1][t-A[i-1]]
                    else:
                        dp[i][j][t] = dp[i-1][j][t]
        return dp[n][k][target]

s = Solution()
print(s.kSum([1,2,3,4], 2, 5))

