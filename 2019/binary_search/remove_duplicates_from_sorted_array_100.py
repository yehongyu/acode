#coding=utf-8

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        n = len(nums)
        if n <= 1:
            return n
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

s = Solution()
print(s.removeDuplicates([]))
print(s.removeDuplicates([1, 1, 2]))




