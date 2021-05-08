#coding=utf-8

class Solution(object):

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def quick_sort(self, nums, start, end):
        if start >= end:
            return
        if start + 1 == end:
            if nums[start] > nums[end]:
                self.swap(nums, start, end)
            return
        mid = start + (end-start)/2
        k = nums[mid]
        self.swap(nums, mid, start)
        i = start; j = end
        while i < j:
            while i <= end and nums[i] <= k: i += 1
            while j >= start and nums[j] > k: j -= 1
            if i < j: self.swap(nums, i, j)
        if j != start:
            self.swap(nums, start, j)
        self.quick_sort(nums, start, j-1)
        self.quick_sort(nums, j, end)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 1:
            return nums
        self.quick_sort(nums, 0, n-1)
        return nums

s = Solution()
print(s.sortArray([5, 2, 3, 1]))
print(s.sortArray([2, 5, 3, 1]))
print(s.sortArray([5, 1, 1, 2, 0, 0]))
