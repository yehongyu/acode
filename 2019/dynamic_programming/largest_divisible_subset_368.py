class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 1: return nums
        nums = sorted(nums)
        dp = [1] * n
        path = [i for i in range(n)]
        max_len = 1; max_end = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] != 0: continue
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    path[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_end = i
        res = [nums[max_end]]
        cur = max_end
        while path[cur] != cur:
            res.insert(0, nums[path[cur]])
            cur = path[cur]
        return res

s = Solution()
print(s.largestDivisibleSubset([3,1,2]))
print(s.largestDivisibleSubset([4,2,8,1]))

