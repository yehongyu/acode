class Solution:
    """
    @param nums:
    @return: nothing
    """
    def maxWeight(self, nums):
        # write your code here
        m = len(nums)
        if m <= 0: return 0
        n = len(nums[0])
        dp