import sys

class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def __init__(self):
        self.max_val = - sys.maxsize - 1

    def helper(self, arr):
        if len(arr) < 3:
            return 0
        if len(arr) == 3:
            return arr[1]
        cur_val = - sys.maxsize - 1
        for i in range(1, len(arr)-1):
            left_arr = arr[0:i+1]
            right_arr = arr[i:]
            #print('begin:', arr, i, cur_val, left_arr, right_arr)
            left = self.helper(left_arr)
            right = self.helper(right_arr)
            val = left + right + arr[i-1] * arr[i] * arr[i+1]
            cur_val = max(cur_val, val)
            print('end:', arr, left, right, val, cur_val)
        return cur_val


    def maxCoins(self, nums):
        # write your code here
        n = len(nums)
        if n <= 0: return -1
        if n == 1: return nums[0]
        arr = [1]
        for i in range(n):
            arr.append(nums[i])
        arr.append(1)
        dp = []
        for i in range(n+2):
            dp.append([0] * (n+2))
        for step in range(2, n+2):
            for j in range(0, n-step+2):
                cur_val = 0
                for k in range(j+1, j+step):
                    cur_val = max(cur_val, dp[j][k] + dp[k][j+step] + arr[j]*arr[k]*arr[j+step])
                dp[j][j+step] = cur_val
        return dp[0][n+1]

s = Solution()
print(s.maxCoins([4, 1, 5, 10]))

