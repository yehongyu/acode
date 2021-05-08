class Solution:
    """
    @param nums: the given array
    @param s: the given target
    @return: the number of ways to assign symbols to make sum of integers equal to target S
    """
    def helper(self, res, nums, s, pos):
        if pos == len(nums) and s == 0:
            res[0] += 1
            return
        if pos >= len(nums):
            return
        for symbol in [-1, 1]:
            cur_s = s - symbol * nums[pos]
            self.helper(res, nums, cur_s, pos+1)

    def findTargetSumWays_recurison(self, nums, s):
        # Write your code here
        n = len(nums)
        res = [0]
        self.helper(res, nums, s, 0)
        return res[0]

    def findTargetSumWays(self, nums, s):
        n = len(nums)
        if n <= 0: return 0
        dp = []
        for i in range(n):
            dp.append([0] * 2001)
        dp[0][nums[0]] += 1
        dp[0][-nums[0]] += 1
        queue1 = set()
        queue1.update([nums[0], -nums[0]])
        for i in range(1, n):
            print(i, queue1)
            qlen = len(queue1)
            queue2 = set()
            for val in queue1:
                cnt = dp[i-1][val]
                tmp = val + nums[i]
                dp[i][tmp] += cnt
                print('first:', i, tmp, dp[i][tmp])
                queue2.add(tmp)
                tmp = val - nums[i]
                dp[i][tmp] += cnt
                queue2.add(tmp)
                print('second', i, tmp, dp[i][tmp])
            queue1 = queue2
        return dp[n-1][s]






s = Solution()
#print(s.findTargetSumWays([1,1,1,1,1], 3))
print(s.findTargetSumWays([0,0,0,0,0,0,0,0,1], 1))
