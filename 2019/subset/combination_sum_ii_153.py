#coding=utf-8

class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """

    def helper(self, res, path, nums, target, start):
        if target == 0:
            res.append(path[0:])
        for i in range(start, len(nums)):
            if target - nums[i] < 0:
                continue
            if i-1>=start and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            self.helper(res, path, nums, target-nums[i], i+1)
            path.pop(len(path)-1)

    def combinationSum2(self, num, target):
        # write your code here
        if target <= 0:
            return [[]]
        res = []
        path = []
        nums = sorted(num)
        self.helper(res, path, nums, target, 0)
        return res

s = Solution()
print(s.combinationSum2([7, 1, 2, 5, 1, 6, 10], 8))

