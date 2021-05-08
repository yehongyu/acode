#coding=utf-8

class Solution(object):

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def maxheadify(self, nums, index, end):
        lnode = 2 * index + 1
        rnode = lnode + 1
        if lnode > end:
            return
        maxidx = lnode
        if rnode <= end and nums[rnode] > nums[lnode]:
            maxidx = rnode
        if nums[maxidx] > nums[index]:
            self.swap(nums, index, maxidx)
            self.maxheadify(nums, maxidx, end)

    def heap_sort(self, nums):
        n = len(nums)
        end = n - 1
        bidx = (end-1)/2
        for i in range(bidx, -1, -1):
            self.maxheadify(nums, i, end)
        for i in range(n-1, 0, -1):
            self.swap(nums, 0, i)
            self.maxheadify(nums, 0, i-1)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 1:
            return nums
        self.heap_sort(nums)
        return nums

s = Solution()
print(s.sortArray([5,3,2,1,4]))
print(s.sortArray([5,1,3,2,1,4,2]))
