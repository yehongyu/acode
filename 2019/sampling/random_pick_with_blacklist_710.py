#coding=utf-8

class Solution1(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.N = N
        self.blacklist = blacklist

    def pick_simple(self):
        import numpy as np
        rnd = np.random.randint(0, self.N)
        while rnd in self.blacklist:
            rnd = np.random.randint(0, self.N)
        return rnd

    def pick_reservior(self):
        """
        :rtype: int
        """
        res = None
        count = 0
        for i in range(self.N):
            if i in self.blacklist:
                continue
            count += 1
            import numpy as np
            index = np.random.randint(0, count)
            if index == 0:
                res = i
        return res

class Solution2(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.map = {}
        self.M = N - len(blacklist)
        print('N:', N)
        print('M:', self.M)
        for i in range(self.M):
            self.map[i] = i
        for b in blacklist:
            if b < self.M:
                N = N - 1
                while N in blacklist:
                    N -= 1
                self.map[b] = N
        print('map:', self.map)

    def pick(self):
        import random
        return self.map[random.randint(0, self.M-1)]

import random
class Solution_mem(object):

    def __init__(self, N, blacklist):
        self.nums = []
        for i in range(N):
            if i not in blacklist:
                self.nums.append(i)

    def pick(self):
        p = random.randint(0, len(self.nums)-1)
        return self.nums[p]

class Solution(object):

    def __init__(self, N, blacklist):
        self.N = N
        self.blacklist = blacklist

    def pick(self):
        res = None
        cnt = 0
        for i in range(N):
            if i in self.blacklist: continue
            p = random.randint(0, cnt)
            if p == 0:
                res = i
            cnt += 1
        return res


# Your Solution object will be instantiated and called as such:
N = 10
blacklist = [5,6]
obj = Solution(N, blacklist)
print(obj.pick())
print(obj.pick())
print(obj.pick())
print(obj.pick())
print(obj.pick())
print(obj.pick())
print(obj.pick())



