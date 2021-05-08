class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * 10001
        for num in nums:
            dp[num] += 1
        for i in range(2, 10001):
            dp[i] = max(dp[i-1], dp[i-2] + dp[i]*i)
        return dp[10000]
