class Solution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums
    """
    def findMin(self, nums):
        # write your code here
        n = len(nums)
        if n <= 0: return 0
        if n == 1: return nums[0]
        if n == 2: return abs(nums[0] - nums[1])
        m = sum(nums)
        dp = [False] * (m+1)
        dp[0] = True
        for num in nums:
            for j in range(m, num-1, -1):
                dp[j] = dp[j] | dp[j-num]
        left = m//2
        right = m//2
        print(dp)
        while left >= 0 and right <= m:
            print(left, dp[left], right, dp[right])
            if dp[right]:
                return abs(m - 2 * right)
            if dp[left]:
                return abs(m - 2 * left)
            left -= 1
            right += 1

s = Solution()
nums = [1, 2, 3, 4]
nums = [1, 6, 11, 5]
print(s.findMin(nums))
