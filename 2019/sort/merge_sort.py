#coding=utf-8

class Solution(object):

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def merge(self, left, right):
        res = []
        m = len(left)
        n = len(right)
        if m <= 0:
            return right
        if n <= 0:
            return left
        i = 0; j = 0
        while i < m and j < n:
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        while i < m:
            res.append(left[i])
            i += 1
        while j < n:
            res.append(right[j])
            j += 1
        return res

    def merge_sort(self, nums, start, end):
        if start >= end:
            return nums[start:end+1]
        if start + 1 == end:
            if nums[start] > nums[end]:
                self.swap(nums, start, end)
            return nums[start:end+1]
        mid = start + (end-start)/2
        left = self.merge_sort(nums, start, mid-1)
        right = self.merge_sort(nums, mid, end)
        res = self.merge(left, right)
        return res

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 1:
            return nums
        return self.merge_sort(nums, 0, n-1)

s = Solution()
print(s.sortArray([5,2,4,3]))
print(s.sortArray([5,2,4,2,3]))
