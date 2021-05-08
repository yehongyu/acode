class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1]*n
        cnt = [1] * n
        max_len = 1; res = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1; cnt[i] = cnt[j]
                    elif dp[j]+1 == dp[i]: cnt[i] += cnt[j]
            max_len = max(dp[i], max_len)
        for i in range(n):
            if dp[i] == max_len:
                res += cnt[i]
        return res

s = Solution()
nums = [1,3,5,4,7]
nums = [2,2,2,2,2]
nums = [1,2,4,3,5,4,7,2]
print(s.findNumberOfLIS(nums))
