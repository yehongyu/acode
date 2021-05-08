#coding=utf-8

class Solution(object):

    def helper(self, res, path, num, k, target, start):
        if len(path) == k and target == 0:
            res.append(path[0:])
        if start > num:
            return
        for i in range(start, num+1):
            if i > target:
                continue
            path.append(i)
            self.helper(res, path, num, k, target-i, i+1)
            path.pop(len(path)-1)

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k <= 0 or n <= 0 or n < k:
            return [[]]
        if k == 1:
            if 1<= n <= 9: return [[n]]
            else: return [[]]
        res = []
        path = []
        self.helper(res, path, 9, k, n, 1)
        return res

s = Solution()
print(s.combinationSum3(3, 7))
print(s.combinationSum3(3, 9))

