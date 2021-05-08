import sys
sys_minint = - sys.maxsize - 1

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray_nxnxk(self, nums, k):
        # write your code here
        n = len(nums)
        if n <= 0:
            return sys_minint
        dp = []
        for i in range(n+1):
            dp.append([sys_minint] * (k+1))
        for i in range(n+1):
            dp[i][0] = 0

        for i in range(1, n+1):
            for j in range(1, min(i+1, k+1)):
                cur_max_sum = 0
                for t in range(i-1, j-2, -1):
                    cur_max_sum = max(cur_max_sum + nums[t], nums[t])
                    dp[i][j] = max(dp[i][j], dp[t][j-1] + cur_max_sum)
        return dp[n][k]

    def maxSubArray_nxn(self, nums, k):
        # write your code here
        n = len(nums)
        if n <= 0 or k > n:
            return sys_minint
        local_s = []
        for i in range(n+1):
            local_s.append([sys_minint] * (k+1))
        global_s = []
        for i in range(n+1):
            global_s.append([sys_minint] * (k+1))
        local_s[0][0] = 0
        global_s[0][0] = 0
        for i in range(1, n+1):
            local_s[i][0] = 0
            global_s[i][0] = 0
            for j in range(1, min(k, i)+1):
                local_s[i][j] = nums[i-1] + max(global_s[i-1][j-1], local_s[i-1][j])
                global_s[i][j] = max(global_s[i-1][j], local_s[i][j])
        return global_s[n][k]

    def maxSubArray_time_nxn_space_n(self, nums, k):
        # write your code here
        n = len(nums)
        if n <= 0 or k > n:
            return sys_minint
        local_s = [sys_minint] * (k+1)
        global_s = [sys_minint] * (k+1)
        for i in range(1, n+1):
            local_s[0] = 0
            global_s[0] = 0
            for j in range(min(k, i), 0, -1):
                local_s[j] = nums[i-1] + max(global_s[j-1], local_s[j])
                global_s[j] = max(global_s[j], local_s[j])
                print(i, j, local_s[j], global_s[j])
            print(i, local_s, global_s)
        return global_s[k]



s = Solution()
print(s.maxSubArray_time_nxn_space_n([1, 2, 3], 1))
print(s.maxSubArray_time_nxn_space_n([-1, 4, -2, 3, -2, 3], 2))
