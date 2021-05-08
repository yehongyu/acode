#coding=utf-8

class Solution(object):


    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def bubble_sort(self, nums):
        n = len(nums)
        changed = True
        while changed:
            i = 0
            changed = False
            while i < n-1:
                if nums[i] > nums[i+1]:
                    self.swap(nums, i, i+1)
                    changed = True
                i += 1

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 1:
            return nums
        self.bubble_sort(nums)
        return nums

s = Solution()
print(s.sortArray([5,3,2,1,4]))
print(s.sortArray([5,1,3,2,1,4,2]))
