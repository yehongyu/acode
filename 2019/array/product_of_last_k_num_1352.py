class ProductOfNumbers(object):

    def __init__(self):
        self.dp = [0]
        self.idx0 = 0

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.idx0 = len(self.dp)
            self.dp.append(0)
        elif self.dp[-1] == 0:
            self.dp.append(num)
        else:
            self.dp.append(self.dp[-1]*num)
        print(self.dp)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        start = len(self.dp) - k -1
        end = len(self.dp)-1
        #print('get:', k, start, end, self.dp)
        if start < self.idx0: return 0
        elif self.dp[start]==0:
            return self.dp[end]
        else:
            return self.dp[end] / self.dp[start]


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
print(obj.getProduct(2))
print(obj.getProduct(3))
print(obj.getProduct(4))
obj.add(8)
print(obj.getProduct(2))
