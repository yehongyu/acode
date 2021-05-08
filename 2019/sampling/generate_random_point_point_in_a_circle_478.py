# coding=utf-8


import math
import random


class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r = radius
        self.x0 = x_center
        self.y0 = y_center

    def randPoint1(self):
        """
        :rtype: List[float]
        """
        p = random.random()
        rnd_r = math.sqrt(random.random()) * self.r
        x = self.x0 + rnd_r * math.cos(p * 2 * math.pi)
        y = self.y0 + rnd_r * math.sin(p * 2 * math.pi)
        return [x, y]

    def randPoint(self):
        """
        :rtype: List[float]
        """
        while True:
            x = 2 * self.r * (random.random() - 0.5)
            y = 2 * self.r * (random.random() - 0.5)
            if x * x + y * y <= self.r * self.r:
                return [self.x0 + x, self.y0 + y]

            # Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()