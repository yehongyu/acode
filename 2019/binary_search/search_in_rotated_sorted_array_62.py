#coding=utf-8

class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search_1(self, A, target):
        # write your code here
        n = len(A)
        if n <= 0:
            return -1
        if n == 1:
            return 0 if A[0] == target else -1
        start = 0; end = n - 1
        while start + 1 < end:
            mid = start + (end-start)/2
            print(start, mid, end)
            if A[mid] == target:
                return mid
            if A[mid] >= A[start]:
                # mid 在左半上升区
                if target >= A[start] and A[mid] > target:
                    end = mid
                else:
                    start = mid
            else:
                # mid 在右半上升区
                if target <= A[end] and A[mid] < target:
                    start = mid
                else:
                    end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1

    def search_I(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0: return -1
        if n == 1: return 0 if nums[0]==target else -1
        l = 0; h=n-1
        while l < h:
            mid = l + (h-l)//2
            if nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    h = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[h]:
                    l = mid
                else:
                    h = mid - 1
        if h >= 0 and nums[h]== target: return h
        if l < n and nums[l]== target: return l
        return -1

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return -1
        if n == 1: return nums[0]
        l = 0; h= n-1
        while l < h:
            if nums[l] < nums[h]: return nums[l]
            mid = l + (h-l)//2
            if nums[mid] > nums[l]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                h = mid
            else:
                l += 1
        return nums[h]


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0: return -1
        if n == 1: return 0 if nums[0]==target else -1
        l = 0; h=n-1
        while l < h:
            mid = l + (h-l)//2
            if nums[mid] == target: return True
            if nums[mid] > nums[l]:
                if nums[l] <= target <= nums[mid]:
                    h = mid
                else:
                    l = mid + 1
            elif nums[mid] < nums[l]:
                if nums[mid] <= target <= nums[h]:
                    l = mid
                else:
                    h = mid - 1
            else:
                l += 1
        if h >= 0 and nums[h]== target: return True
        if l < n and nums[l]== target: return True
        return False

s = Solution()
'''
print(s.search([4, 5, 1, 2, 3], 1))
print(s.search([4, 5, 1, 2, 3], 0))
print(s.search([6,8,9,1,3,5], 5))
print(s.search([5,1,3], 3))
print(s.findMin([5,1,3]))
print(s.findMin([3,4,5,1,2]))
print(s.findMin([4,5,6,7,0,1,2]))
print(s.findMin([2,2,2,0,1]))
'''
nums = [2,5,6,0,0,1,2]; target = 0
print(s.search(nums, target))
nums = [2,5,6,0,0,1,2]; target = 3
print(s.search(nums, target))
