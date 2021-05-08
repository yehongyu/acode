class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1: return 0
        pre = 0; res = 0
        for i in range(1, n):
            cur = prices[i] - prices[i-1]
            if pre > 0: cur += pre
            res = max(res, cur)
            pre = cur
        return res

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1: return 0
        pre = 0; res = 0
        left = [0]
        for i in range(1, n):
            cur = prices[i] - prices[i-1]
            if pre > 0: cur += pre
            res = max(res, cur)
            left.append(res)
            pre = cur

        pre = 0; res = 0
        right = [0]
        for i in range(n-2, -1, -1):
            cur = prices[i+1] - prices[i]
            if pre > 0: cur += pre
            res = max(res, cur)
            right.insert(0, res)
            pre = cur
        res = max(left[-1], right[0])
        for i in range(n-1):
            cur = left[i] + right[i+1]
            res = max(cur, res)
        return res

s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))
