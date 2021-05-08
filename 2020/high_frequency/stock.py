class Solution(object):
    # easy
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if size <= 1: return 0
        if size == 2: return max(0, prices[1]-prices[0])
        max_profit = 0
        pre = 0
        for i in range(1, size):
            cur = prices[i]-prices[i-1]
            if pre >= 0:
                cur = pre + prices[i]-prices[i-1]
            max_profit = max(max_profit, cur)
            pre = cur
        return max_profit

    # hard
    def maxProfit_TwiceTransaction(self, prices):
        size = len(prices)
        if size <= 1: return 0
        if size == 2: return max(0, prices[1]-prices[0])
        pre = 0
        left = [0] * size # left max profit
        for i in range(1, size):
            cur = prices[i] - prices[i-1]
            if pre > 0:
                cur = cur + pre
            left[i] = max(left[i-1], cur)
            pre = cur
        pre = 0
        right = [0] * size # right max profit
        for i in range(size-2, -1, -1):
            cur = prices[i+1] - prices[i]
            if pre > 0:
                cur = cur + pre
            right[i] = max(right[i+1], cur)
            pre = cur
        max_profit = max(max(left), max(right))
        for i in range(1, size-1):
            max_profit = max(max_profit, left[i] + right[i+1])
        return max_profit

    # hard
    def maxProfit_KTransaction(self, k, prices):
        pass



if __name__ == "__main__":
    s = Solution()
    prices = [7,6,4,3,1] # res=0
    prices = [7,1,5,3,6,4] # res=5
    #res = s.maxProfit(prices)

    prices = [3,3,5,0,0,3,1,4] # res=6
    prices = [1,2,3,4,5] # res=4
    res = s.maxProfit_TwiceTransaction(prices)
    print("max profit:", res)

