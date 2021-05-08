#coding=utf-8

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return nums[0]
        start = 0
        end = n - 1
        while start + 1 < end:
            mid = start + (end-start)/2
            if nums[mid] > nums[end]:
                start = mid
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end -= 1
        return min(nums[start], nums[end])

s = Solution()
print(s.findMin([2, 1]))
print(s.findMin([4,4,5,6,7,0,1,2]))
