#coding=utf-8

class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def reverse(self, nums, start, end):
        if start >= end:
            return
        mid = (end-start)/2
        for i in range(mid+1):
            tmp = nums[start+i]
            nums[start+i] = nums[end-i]
            nums[end-i] = tmp

    def recoverRotatedSortedArray(self, nums):
        # write your code here
        n = len(nums)
        if n <= 1:
            return
        pos = -1
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                pos = i
                break
        if pos == -1:
            return
        self.reverse(nums, 0, pos-1)
        self.reverse(nums, pos, n-1)
        self.reverse(nums, 0, n-1)

s = Solution()
nums = [4, 5, 1, 2, 3]
s.recoverRotatedSortedArray(nums)
print('res:', nums)
nums = [6,8,9,1,2]
s.recoverRotatedSortedArray(nums)
print('res', nums)
nums = [1, 2, 6,8,9]
s.recoverRotatedSortedArray(nums)
print('res', nums)
