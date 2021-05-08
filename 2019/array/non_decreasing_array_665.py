class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n <= 2: return True
        flag = False
        for i in range(0, n-1):
            if nums[i] <= nums[i+1]: continue
            if flag: return False
            flag = True
            if i-1<0 or nums[i-1] <= nums[i+1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
        return True

s = Solution()
nums = [4,2,3]
nums = [4,2,1]
print(s.checkPossibility(nums))
