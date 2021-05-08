class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        start = 0
        for i in range(1, n):
            if nums[i] - nums[i-1] == 1: continue
            if i - start < 3: return False
            start = i
        return True
s = Solution()
nums = [1,2,3,3,4,5]
print(s.isPossible(nums))
nums = [1,2,3,3,4, 4,5, 5]
print(s.isPossible(nums))
