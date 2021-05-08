#coding=utf-8
import numpy as np
import random

class Solution1(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.minx, self.miny, _, _ = np.amin(np.array(rects), 0)
        _, _, self.maxx, self.maxy = np.amax(np.array(rects), 0)

    def in_rects(self, x, y):
        for item in self.rects:
            if item[0] <= x <= item[2] \
                    and item[1] <= y <= item[3]:
                return True
        return False

    def pick(self):
        """
        :rtype: List[int]
        """
        while True:
            x = random.randint(self.minx, self.maxx)
            y = random.randint(self.miny, self.maxy)
            if self.in_rects(x, y):
                return [x, y]

class Solution_2(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.sum = [0] * len(rects)
        for i in range(len(rects)):
            rect = rects[i]
            area = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            if i == 0:
                self.sum[i] = area
            else:
                self.sum[i] = self.sum[i-1] + area

    def pick(self):
        """
        :rtype: List[int]
        """
        import random
        rnd = random.randint(1, self.sum[-1])
        low = 0
        high = len(self.sum) - 1
        while low < high:
            mid = low + (high-low)/2
            if self.sum[mid] < rnd:
                low = mid + 1
            else:
                high = mid
        rect = self.rects[high]
        x = random.randint(rect[0], rect[2])
        y = random.randint(rect[1], rect[3])
        return [x, y]

class Solution_3(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects[0:]
        self.sum = [0] * len(rects)
        for i in range(len(rects)):
            rect = rects[i]
            area = (rect[2]-rect[0]+1) * (rect[3]-rect[1]+1)
            if i == 0:
                self.sum[i] = area
            else:
                self.sum[i] = self.sum[i-1] + area

    def pick_sampling(self):
        """
        :rtype: List[int]
        """
        n = len(self.rects)
        res = None
        cnt = 0
        for i in range(n):
            rect = self.rects[i]
            for j in range(rect[0], rect[2]+1):
                for k in range(rect[1], rect[3]+1):
                    p = random.randint(0, cnt)
                    if p == 0:
                        res = [j, k]
                    cnt += 1
        return res

    def pick_binary_search(self):
        rnd = random.randint(1, self.sum[-1])
        low = 0; high = len(self.sum) -1
        while low < high:
            mid = low + int((high-low)//2)
            if self.sum[mid] < rnd:
                low = mid + 1
            else:
                high = mid
        rect = self.rects[high]
        x = random.randint(rect[0], rect[2])
        y = random.randint(rect[1], rect[3])
        return [x, y]

class Solution(object):
    def get_first_large_pos(self, nums, val):
        l = 0; h = len(nums)-1
        while l < h:
            mid = l + (h-l)//2
            if nums[mid] < val:
                l = mid + 1
            else:
                h = mid
        return h

    def median_of_samples(self, count):
        n = len(count)
        acc = [0] * n
        for i in range(n):
            if i == 0:
                acc[i] = count[i]
            else:
                acc[i] = acc[i-1] + count[i]
        total = acc[-1]
        if total % 2 == 1:
            pos = self.get_first_large_pos(acc, (total + 1)//2)
            print(pos)
            return pos
        else:
            mid = total // 2
            pos1 = self.get_first_large_pos(acc, mid)
            pos2 = self.get_first_large_pos(acc, mid+1)
            print(pos1, pos2)
            return (pos1 + pos2) / 2



# Your Solution object will be instantiated and called as such:

s = Solution()
count = [3,2,4,0,1]
print(s.median_of_samples(count))
'''
rects = [[1,1,5,5], [-2,-2,-1,-1]]
obj = Solution(rects)
print(obj.pick())
print(obj.pick())
print(obj.pick())

'''
