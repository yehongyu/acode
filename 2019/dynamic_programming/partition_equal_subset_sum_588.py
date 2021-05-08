class Solution:
    """
    @param nums: a non-empty array only positive integers
    @return: true if can partition or false
    """
    def canPartition(self, nums):
        # write your code here
        n = len(nums)
        if n <= 1: return False
        if n == 2: return nums[0] == nums[1]
        m = sum(nums)
        if m % 2 != 0: return False
        m = m // 2
        dp = [False] * (m+1)
        dp[0] = True
        for num in nums:
            for j in range(m, num-1, -1):
                dp[j] = dp[j] | dp[j-num]
        return dp[m]

s = Solution()
nums = [1, 5, 11, 5]
nums = [1, 2, 3, 9]
print(s.canPartition(nums))
