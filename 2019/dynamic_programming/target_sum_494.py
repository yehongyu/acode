class Solution(object):
    def subsetSum(self, nums, target):
        n = len(nums)
        if n <= 0: return 0
        dp = [0] * (target+1)
        dp[0] = 1
        for num in nums:
            for j in range(target, -1, -1):
                if j-num>=0:
                    dp[j] += dp[j-num]
        return dp[target]

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        if n <= 0: return 0
        acc = sum(nums)
        target2 = S + acc
        if target2 % 2 == 1: return 0
        return self.subsetSum(nums, target2//2)

s = Solution()
nums = [1, 1, 1, 1, 1]
S = 3
print(s.findTargetSumWays(nums, S))