class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        dp = [0] * n
        for i in range(n):
            curMax = 0
            step = 1
            while step <= K and i-step+1 >= 0:
                curMax = max(curMax, A[i-step+1])
                if i < K:
                    cur_val = curMax * step
                else:
                    cur_val = dp[i-step] + curMax * step
                dp[i] = max(dp[i], cur_val)
                step += 1
        return dp[n-1]

s = Solution()
A = [1,15,7,9,2,5,10]; K = 3
print(s.maxSumAfterPartitioning(A, K))



