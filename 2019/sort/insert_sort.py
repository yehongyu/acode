#coding=utf-8

class Solution(object):

    def insert_sort(self, nums):
        n = len(nums)
        for i in range(1, n):
            k = nums[i]
            j = 0
            while j < i and nums[j] <= k:
                j += 1
            pos = j
            for j in range(i-1, pos-1, -1):
                nums[j+1] = nums[j]
            if pos < i:
                nums[pos] = k

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 1:
            return nums
        self.insert_sort(nums)
        return nums

s = Solution()
print(s.sortArray([5,3,2,1,4]))
print(s.sortArray([5,1,3,2,1,4,2]))
