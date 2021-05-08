#coding=utf-8

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def helper(self, res, path, nums, pos):
        res.append(path[0:])
        print('pos=', pos, 'path=', path, 'res=', res)
        for i in range(pos, len(nums)):
            path.append(nums[i])
            self.helper(res, path, nums, i+1)
            path.pop(len(path)-1)

    def subsets(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [[], nums]
        nums = sorted(nums)
        path = []
        res = []
        self.helper(res, path, nums, 0)
        return res

s = Solution()
print(s.subsets([0, 1, 2]))
