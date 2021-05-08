class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 0: return 0
        if n == 1: return nums[0]
        pre = res = nums[0]
        for i in range(1, n):
            cur = nums[i]
            if pre > 0:
                cur += pre
            res = max(res, cur)
            pre = cur
        return res
