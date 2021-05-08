class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n<= 1: return []
        res = []
        for i in range(n):
            cur = abs(nums[i])
            if nums[cur-1] < 0:
                res.append(cur)
            else:
                nums[cur-1] = -nums[cur-1]
        return res

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 0: return []
        for i in range(n):
            cur = abs(nums[i])
            if nums[cur-1] > 0:
                nums[cur-1] = -nums[cur-1]
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        return res

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            cur = abs(nums[i])
            if cur == 0: self.swap(nums, cur, i)
            cur = abs(nums[i])
            if cur < n and nums[cur] >= 0:
                nums[cur] = -nums[cur]
            print(nums)
        for i in range(n):
            if nums[i] > 0:
                return i
        return n


s = Solution()
nums = [9,6,4,2,3,5,7,0,1]
nums = [2,0]
nums = [9,6,4,2,3,5,7,0,1]
print(s.missingNumber(nums))

'''
nums = [4,3,2,7,8,2,3,1]
print(s.findDuplicates(nums))
'''

