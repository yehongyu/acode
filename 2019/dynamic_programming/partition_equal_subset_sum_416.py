class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        acc = sum(nums)
        if acc % 2 == 1: return False
        target = acc // 2
        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            for i in range(target, 0, -1):
                if i - num >=0:
                    dp[i] |= dp[i-num]
        return dp[target]

s = Solution()
print(s.canPartition([1,2,3,5]))
print(s.canPartition([1,5,11,5]))


