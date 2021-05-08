class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing_SUM(self, nums):
        # write your code here
        n = len(nums)
        curSum = 0
        trueSum = n
        for i in range(n):
            trueSum += i
            curSum += nums[i]
        return trueSum - curSum

    def findMissing(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            print('be:', i, nums[i])
            if nums[i] != i and nums[i] < n:
                print(i, nums[i])
                tmp1 = nums[i]
                tmp2 = nums[tmp1]
                nums[i] = tmp2
                nums[tmp1] = tmp1
                i -= 1
            i += 1
            print(nums)
        for i in range(n):
            if nums[i] != i:
                return i
        return n

s = Solution()
print(s.findMissing([9,8,7,6,2,0,1,5,4]))
