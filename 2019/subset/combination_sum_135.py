# coding=utf-8

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def helper(self, res, path, candidates, target, start):
        if target == 0:
            res.append(path[0:])
        for i in range(start, len(candidates)):
            if target - candidates[i] < 0:
                continue
            if i-1>=start and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            self.helper(res, path, candidates, target-candidates[i], i)
            path.pop(len(path)-1)

    def combinationSum(self, candidates, target):
        # write your code here
        if target <= 0:
            return [[]]
        res = []
        path = []
        candidates = sorted(candidates)
        self.helper(res, path, candidates, target, 0)
        return res

s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([2, 2, 3], 5))




