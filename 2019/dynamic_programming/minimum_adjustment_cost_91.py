# coding=utf-8
import sys

class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """

    def helper(self, A, B, dp, target, index):
        if index == len(A):
            return 0
        diff = 0
        min_diff = sys.maxsize
        for val in range(0, 101):
            if index != 0 and abs(val - B[index-1]) > target:
                continue
            if dp[index][val] != sys.maxsize:
                diff = dp[index][val]
                min_diff = min(min_diff, diff)
                continue
            B.append(val)
            diff = abs(val - A[index])
            diff += self.helper(A, B, dp, target, index+1)
            min_diff = min(min_diff, diff)
            B.pop(-1)
            dp[index][val] = diff
            print(index, val, diff, B)
        return min_diff


    def MinAdjustmentCost_rec(self, A, target):
        # write your code here
        n = len(A)
        if n <= 1:
            return 0
        B = []
        dp = []
        for i in range(n):
            dp.append([sys.maxsize] * 101)
        res = self.helper(A, B, dp, target, 0)
        print(min(dp[n-1]))
        return res

    def MinAdjustmentCost(self, A, target):
        n = len(A)
        if n <= 1: return 0
        dp = []
        for i in range(n):
            dp.append([sys.maxsize] * 101)
        for i in range(n):
            for j in range(101):
                for val in range(max(j-target, 0), min(j+target, 100)+1):
                    if i==0:
                        dp[i][j] = min(dp[i][j], abs(j-A[i]))
                    else:
                        dp[i][j] = min(dp[i][j], dp[i-1][val] + abs(j-A[i]))
                print(i, j, val, dp[i][j])
        return min(dp[n-1])




s = Solution()
#print(s.MinAdjustmentCost([1, 4, 2, 3], 1))
#print(s.MinAdjustmentCost([3, 5, 4, 7], 2))
print(s.MinAdjustmentCost([12,3,7,4,5,13,2,8,4,7,6,5,7], 2))
