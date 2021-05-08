class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset
    """
    def largestDivisibleSubset(self, nums):
        # write your code here
        n = len(nums)
        if n <= 1: return nums
        dp = [0] * n
        parent = [i for i in range(n)]
        max_len = 1; max_idx = n-1
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if nums[j] % nums[i] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if dp[i] > max_len:
                        max_len = dp[i]; max_idx = i
        res = []
        cur = max_idx
        print(max_idx, parent, dp)
        while cur != parent[cur]:
            res.append(nums[cur])
            cur = parent[cur]
        res.append(nums[cur])
        return res

s = Solution()
print(s.largestDivisibleSubset([1,2,3]))


