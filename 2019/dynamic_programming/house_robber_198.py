class Solution(object):
    def rob_i(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 0: return 0
        if n == 1: return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, n):
            if i-2 >= 0:
                dp[i] = dp[i-2]
            if i-3 >= 0:
                dp[i] = max(dp[i], dp[i-3])
            dp[i] += nums[i]
            res = max(res, dp[i])
        return res

    def dfs(self, root, mem):
        if root == None: return 0
        if root in mem: return mem[root]
        val1 = 0
        if root.left:
            val1 += self.dfs(root.left.left, mem) + self.dfs(root.left.right, mem)
        if root.right:
            val1 += self.dfs(root.right.left, mem) + self.dfs(root.right.right, mem)
        val1 += root.val
        val2 = self.dfs(root.left, mem) + self.dfs(root.right, mem)
        val = max(val1, val2)
        mem[root] = val
        return val

    def rob(self, root):
        mem = {}
        return self.dfs(root, mem)

s = Solution()
nums = [1,2,3,1]
nums = [2,7,9,3,1]
print(s.rob(nums))

