class Solution(object):
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def reverse(self, nums, l, h):
        while l < h:
            self.swap(nums, l, h)
            l += 1; h -= 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1: return
        i = n - 2; pos = None
        while i >= 0:
            if nums[i] >= nums[i+1]:
                i -= 1
            else:
                pos = i
                break
        if pos != None:
            i = pos + 1
            while i<n and nums[i] > nums[pos]: i += 1
            self.swap(nums, pos, i-1)
            self.reverse(nums, pos+1, len(nums)-1)
        else:
            self.reverse(nums, 0, len(nums)-1)

s = Solution()
nums = [1,3,2]
s.nextPermutation(nums)
print(nums)

'''
nums = [3,2,1]
s.nextPermutation(nums)
print(nums)
nums = [1,1,5]
s.nextPermutation(nums)
print(nums)
'''
