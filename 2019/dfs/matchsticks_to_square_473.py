class Solution(object):

    def dfs(self, nums, path, target, pos):
        n = len(nums)
        if pos == n:
            res = True
            for val in path:
                if val != target: res = False
            return res
        for i in range(4):
            if nums[pos] + path[i] <= target:
                path[i] += nums[pos]
                if self.dfs(nums, path, target, pos+1):
                    return True
                path[i] -= nums[pos]
        return False

    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 4: return False
        total = sum(nums)
        if total % 4 != 0: return False
        target = total / 4
        path = [0] * 4
        nums = sorted(nums, reverse=True)
        print(nums)
        return self.dfs(nums, path, target, 0)

s = Solution()
nums = [3,3,3,3,4]
print(s.makesquare(nums))