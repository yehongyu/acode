#coding=utf-8

class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def helper(self, res, path, nums, visited):
        n = len(nums)
        if len(path) == n:
            res.append(path[0:])
        for i in range(n):
            if visited[i] == 1:
                continue
            if i-1 >=0 and nums[i] == nums[i-1] and visited[i-1] == 0:
                continue
            visited[i] = 1
            path.append(nums[i])
            self.helper(res, path, nums, visited)
            path.pop(len(path)-1)
            visited[i] = 0


    def permuteUnique(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return [[]]
        if n == 1:
            return [nums]
        nums = sorted(nums)
        res = []
        path = []
        visited = [0] * n
        self.helper(res, path, nums, visited)
        return res

s = Solution()
print(s.permuteUnique([1, 2, 2]))