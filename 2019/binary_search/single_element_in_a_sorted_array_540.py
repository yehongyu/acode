class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return None
        if n == 1: return nums[0]
        l = 0; r=n-1
        while l < r:
            mid = l + (r-l)//2
            if mid % 2 == 1:mid -=1
            if nums[mid] != nums[mid+1]:
                r = mid
            else: l = mid + 2
        return nums[r]

s = Solution()
nums = [1,1,2,3,3,4,4,8,8]
print(s.singleNonDuplicate(nums))

