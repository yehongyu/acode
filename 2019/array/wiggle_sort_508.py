class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    def wiggleSort(self, nums):
        # write your code here
        n = len(nums)
        if n <= 1: return
        for i in range(n-1):
            if i % 2 == 0:
                if nums[i] > nums[i+1]:
                    self.swap(nums, i, i+1)
            else:
                if nums[i] < nums[i+1]:
                    self.swap(nums, i, i+1)

s = Solution()
nums = [1,5,1,1,6,4]
s.wiggleSort(nums)

print(nums)

