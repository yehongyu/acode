class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 1
        if n == 1: return 1 if nums[0] != 1 else 2
        for i in range(n):
            while nums[i]>0 and nums[i]<=n and \
                nums[nums[i]-1] != nums[i]:
                self.swap(nums, i, nums[i]-1)
        for i in range(n):
            if nums[i] != i+1: return i+1
        return n+1

s = Solution()
print(s.firstMissingPositive([1,2,0]))


