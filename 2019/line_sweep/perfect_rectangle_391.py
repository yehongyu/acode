#coding=utf-8

class Solution(object):

    def gen_point(self, x, y):
        return str(x) + '-' + str(y)
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        if len(rectangles) <= 1:
            return True
        minleft, mindown, maxright, maxup = rectangles[0][0:4]
        points = set()
        sum = 0
        for i in range(0, len(rectangles)):
            rect = rectangles[i]
            sum += (rect[3]-rect[1]) * (rect[2]-rect[0])
            minleft = min(minleft, rect[0])
            mindown = min(mindown, rect[1])
            maxright = max(maxright, rect[2])
            maxup = max(maxup, rect[3])
            ldown = self.gen_point(rect[0], rect[1])
            lup = self.gen_point(rect[0], rect[3])
            rdown = self.gen_point(rect[2], rect[1])
            rup = self.gen_point(rect[2], rect[3])
            if ldown not in points:
                points.add(ldown)
            else:
                points.remove(ldown)
            if lup not in points:
                points.add(lup)
            else:
                points.remove(lup)
            if rdown not in points:
                points.add(rdown)
            else:
                points.remove(rdown)
            if rup not in points:
                points.add(rup)
            else:
                points.remove(rup)
        if len(points) != 4:
            return False
        if self.gen_point(minleft, mindown) not in points:
            return False
        if self.gen_point(minleft, maxup) not in points:
            return False
        if self.gen_point(maxright, mindown) not in points:
            return False
        if self.gen_point(maxright, maxup) not in points:
            return False
        totalSum = (maxup - mindown) * (maxright - minleft)
        return totalSum == sum

s = Solution()
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]
print(s.isRectangleCover(rectangles))
rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]
print(s.isRectangleCover(rectangles))
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]
print(s.isRectangleCover(rectangles))
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]
print(s.isRectangleCover(rectangles))

