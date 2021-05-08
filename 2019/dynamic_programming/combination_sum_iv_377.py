class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n <= 0 or target < 0: return 0
        if target == 0: return 1
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for j in range(n):
                if i-nums[j] >= 0 and dp[i-nums[j]] > 0:
                    dp[i] += dp[i-nums[j]]
        return dp[target]

s = Solution()
nums = [1,2,3]
target = 4
print(s.combinationSum4(nums, target))
