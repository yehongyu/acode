class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3: return False
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] == nums[j] + 1:
                    dp[i] = max(dp[i], dp[j]+1)

