class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n <= 0: return False
        if n == 1: return True
        dp = []
        for i in range(n):
            dp.append([0] * n)
            dp[i][i] = nums[i]
        for step in range(1, n):
            for i in range(0, n-step):
                j = i + step
                print(dp[i+1][j])
                print(dp[i][j-1])
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        return dp[0][n-1] >= 0

s = Solution()
print(s.PredictTheWinner([1,5,2]))
print(s.PredictTheWinner([1,5,233,7]))
print(s.PredictTheWinner([1,1]))
