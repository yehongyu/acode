#coding=utf-8

class Solution(object):

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def select_sort(self, nums):
        n = len(nums)
        for i in range(0, n):
            k = i
            mink = nums[i]
            for j in range(i+1, n):
                if nums[j] < mink:
                    mink = nums[j]
                    k = j
            if k > i:
                self.swap(nums, k, i)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 1:
            return nums
        self.select_sort(nums)
        return nums

s = Solution()
print(s.sortArray([5,3,2,1,4]))
print(s.sortArray([5,1,3,2,1,4,2]))
