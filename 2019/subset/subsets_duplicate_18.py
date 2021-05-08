#coding=utf-8

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def helper(self, res, path, nums, pos):
        res.append(path[0:])
        for i in range(pos, len(nums)):
            if i-1>=0 and i-1 >= pos and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.helper(res, path, nums, i+1)
            path.pop(len(path)-1)


    def subsetsWithDup(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return [[]]
        if n == 1:
            return [[], nums]
        nums = sorted(nums)
        res = []
        path = []
        self.helper(res, path, nums, 0)
        return res

s = Solution()
print(s.subsetsWithDup([1, 2, 2]))