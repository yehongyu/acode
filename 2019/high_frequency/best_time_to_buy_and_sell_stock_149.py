class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        n = len(prices)
        min_left = prices[0]
        max_profit = 0
        for i in range(1, n):
            cur = prices[i] - min_left
            max_profit = max(max_profit, cur)
            min_left = min(prices[i], min_left)
        return max_profit

    def maxProfit_II(self, prices):
        n = len(prices)
        profit = 0
        for i in range(1, n):
            cur = prices[i] - prices[i-1]
            if cur > 0:
                profit += cur
        return profit

    def maxProfit_III(self, prices):
        n = len(prices)
        if len(prices) <= 1:
            return 0
        if len(prices) <= 2:
            return max(0, prices[1]-prices[0])
        min_left = prices[0]
        left = [0]
        for i in range(1, n):
            cur = prices[i] - min_left
            if cur > left[-1]:
                left.append(cur)
            else:
                left.append(left[-1])
            if prices[i] < min_left:
                min_left = prices[i]

        max_right = prices[-1]
        right = [0]
        for i in range(n-2, -1, -1):
            cur = max_right - prices[i]
            if cur > right[0]:
                right.insert(0, cur)
            else:
                right.insert(0, right[0])
            if prices[i] > max_right:
                max_right = prices[i]
        print("left:", left)
        print("right:", right)
        res = max(right[0], left[-1])
        print('tmp res:', res)
        for i in range(1, n-1):
            cur = left[i] + right[i+1]
            res = max(res, cur)
            print('res=', i, cur, res)
        return res

    def maxProfit_III_simple(self, prices):
        n = len(prices)
        if n <= 1:
            return 0
        left_profit = [0]
        min_price = prices[0]
        cur_profit = 0
        for i in range(1, n):
            cur_profit = max(prices[i]-min_price, cur_profit)
            left_profit.append(cur_profit)
            if prices[i] < min_price:
                min_price = prices[i]

        right_profit = [0]
        max_price = prices[n-1]
        cur_profit = 0
        for i in range(n-2, -1, -1):
            cur_profit = max(max_price - prices[i], cur_profit)
            right_profit.insert(0, cur_profit)
            if prices[i] > max_price:
                max_price = prices[i]
        print(left_profit)
        print(right_profit)
        res = max(left_profit[n-1], right_profit[0])
        for i in range(0, n-1):
            res = max(res, left_profit[i] + right_profit[i+1])
        return res



    def maxProfit_IV(self, K, prices):
        n = len(prices)
        if K >= n:
            return self.maxProfit_II(prices)
        local_dp = [0] * (K+1)
        global_dp = [0] * (K+1)

        for i in range(0, n-1):
            diff = prices[i+1] - prices[i]
            for j in range(K, 0, -1):
                local_dp[j] = max(global_dp[j-1] + max(diff, 0), local_dp[j] + diff)
                global_dp[j] = max(global_dp[j], local_dp[j])
                print(i, j, local_dp, global_dp)
        return global_dp[K]



s = Solution()
'''
print(s.maxProfit([3, 2, 3, 1, 2]))
print(s.maxProfit([1, 2, 3, 4, 5]))
print(s.maxProfit([5, 4, 3, 2, 1]))

print(s.maxProfit_II([2, 1, 2, 0, 1]))
'''
#print(s.maxProfit_III([4,4,6,1,1,4,2,5]))
#print(s.maxProfit_III_simple([4,4,6,1,1,4,2,5]))
#print(s.maxProfit_III_simple([3,2,6,5,0,3]))
#print(s.maxProfit_III([3,2,6,5,0,3]))
#print(s.maxProfit_III([1,2,4]))
#print(s.maxProfit_IV(2, [4, 4, 6, 1, 1, 4, 2, 5]))

#print(s.maxProfit_IV(2, [4, 4, 6, 1, 1, 4, 2, 5]))
print(s.maxProfit_IV(1, [3,4,8,5]))
#print(s.maxProfit_IV(1, [3, 2, 1]))
