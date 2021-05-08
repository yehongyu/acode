#coding=utf-8

class Solution1(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.sum = w[0:]
        if len(w) <= 0:
            return
        for i in range(1, len(w)):
            self.sum[i] = self.sum[i-1] + w[i]
        print(self.sum)

    def pickIndex(self):
        """
        :rtype: int
        """
        import numpy as np
        rnd = np.random.randint(0, self.sum[-1])
        low = 0
        high = len(self.sum) - 1
        while low < high:
            mid = low + (high-low)/2
            if self.sum[mid] <= rnd:
                low = mid + 1
            elif self.sum[mid] > rnd+1:
                high = mid
            else:
                return mid
        return high

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w[0:]

    def pickIndex(self):
        """
        :rtype: int
        """
        import numpy as np
        res = None
        count = 0
        for i in range(len(self.w)):
            w = self.w[i]
            for j in range(0, w):
                count += 1
                if np.random.randint(0, count) == 0:
                    res = i
        return res

import random
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w[0:]

    def pickIndex(self):
        n = len(self.w)
        res = None; cnt = 0
        for i in range(n):
            for j in range(self.w[i]):
                p = random.randint(0, cnt)
                if p == 0: res = i
                cnt += 1
        return res

# Your Solution object will be instantiated and called as such:
w = [3, 14, 1, 7]
obj = Solution(w)
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
