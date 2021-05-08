class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0: return [-1, -1]
        if n == 1: return [-1, -1] if nums[0] != target else [0, 0]
        import sys
        nums.append(sys.maxsize)
        n = len(nums)
        l = 0; h=n-1
        while l < h:
            mid = l + (h-l)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                h = mid
        if nums[l] != target: return [-1, -1]
        left = l
        l = 0; h=n-1
        while l < h:
            print('be', l, h)
            mid = l + (h-l)//2
            if nums[mid] <= target:
                l = mid + 1
            else:
                h = mid
            print('end', l, h)
        return [left, l-1]

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import sys
        nums.append(sys.maxsize)
        n = len(nums)
        l = 0; h = n-1
        while l < h:
            mid = l + (h-l)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                h = mid
        return l


s = Solution()
'''
nums = [2,2]; target = 2
nums = [5,7,7,8,8,10]; target = 8
print(s.searchRange(nums, target))
'''
nums = [1,3,5,6]; target = 7
print(s.searchInsert(nums, target))


