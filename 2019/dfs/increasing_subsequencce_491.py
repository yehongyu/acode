class Solution(object):

    def dfs(self, nums, res, path, pos):
        print(pos, path)
        n = len(nums)
        if len(path) >= 2:
            res.append(path[0:])
        if pos >= n: return
        unq = set()
        for i in range(pos, n):
            if nums[i] in unq: continue
            if len(path) == 0 or path[-1] <= nums[i]:
                unq.add(nums[i])
                path.append(nums[i])
                self.dfs(nums, res, path, i+1)
                path.pop(-1)


    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        path = []
        res = []
        self.dfs(nums, res, path, 0)
        return res

s = Solution()
print(s.findSubsequences([4,6,7,7]))
