import math
class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum_loop(self, n):
        # Write your code here
        dice1 = {0:1}
        for i in range(n):
            dice2 = {}
            for j in range(1, 7):
                for key in dice1.keys():
                    if key + j not in dice2:
                        dice2[key+j] = dice1[key] / float(6)
                    else:
                        dice2[key+j] += dice1[key] / float(6)
            dice1 = dice2
        res = []
        for key in dice1.keys():
            res.append([key, dice1[key]])
        return res

    def dicesSum(self, n):
        dp = []
        for i in range(n): dp.append([0] * (6 * n + 1))
        for j in range(1,7): dp[0][j] = 1
        div_num = 6
        for i in range(1, n):
            div_num *= 6
            for j in range(1, 6*n+1):
                for k in range(1, 7):
                    if j-k >= 0: dp[i][j] += dp[i-1][j-k]
        res = []
        for j in range(1, 6*n+1):
            if dp[n-1][j] > 0:
                res.append([j, dp[n-1][j] / float(div_num)])
        return res

s = Solution()
print(s.dicesSum(2))



