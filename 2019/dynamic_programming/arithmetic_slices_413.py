class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3: return 0
        dp = [0] * n
        if A[2]-A[1] == A[1]-A[0]: dp[2] = 1
        res = dp[2]
        for i in range(3, n):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp[i] = dp[i-1] + 1
            res += dp[i]
        return res

s = Solution()

print(s.numberOfArithmeticSlices([1,2,3,4]))
