#coding=utf-8

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    ## *************** permute,dfs, in ******************
    def helper(self, res, path, nums):
        n = len(nums)
        if len(path) == n:
            res.append(path[0:])
        for i in range(0, n):
            if nums[i] in path:
                continue
            path.append(nums[i])
            self.helper(res, path, nums)
            path.pop(len(path)-1)

    def permute(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [nums]
        res = []
        path = []
        self.helper(res, path, nums)
        return res

    ## *************** permute, dfs, visited ******************
    def helper_dfs_visited(self, res, path, nums, visited):
        n = len(nums)
        if len(path) == n:
            res.append(path[0:])
        for i in range(n):
            if visited[i] == 1:
                continue
            visited[i] = 1
            path.append(nums[i])
            self.helper_dfs_visited(res, path, nums, visited)
            path.pop(len(path)-1)
            visited[i] = 0

    def permute_dfs_visited(self, nums):
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [nums]
        res = []
        path = []
        visited = [0] * n
        self.helper_dfs_visited(res, path, nums, visited)
        return res

    ## *************** permute, swap ******************
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def helper_swap(self, res, nums, start):
        if start == len(nums):
            res.append(nums[0:])
        for i in range(start, len(nums)):
            self.swap(nums, start, i)
            self.helper_swap(res, nums, start+1)
            self.swap(nums, start, i)

    def permute_swap(self, nums):
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [nums]
        res = []
        self.helper_swap(res, nums, 0)
        return res


s = Solution()
#print(s.permute([0, 1, 2]))
#print(s.permute_swap([0, 1, 2]))
print(s.permute_dfs_visited([0, 1, 2]))
