class Solution(object):

    def check(self, radius, x_center, y_center, x, y):
        return (x-x_center) * (x-x_center) + (y-y_center)*(y-y_center) <= radius * radius

    def checkOverlap(self, radius, x_center, y_center, x1, y1, x2, y2):
        """
        :type radius: int
        :type x_center: int
        :type y_center: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        if self.check(radius, x_center, y_center, x1, y1):
            return True
        if self.check(radius, x_center, y_center, x1, y2):
            return True
        if self.check(radius, x_center, y_center, x2, y1):
            return True
        if self.check(radius, x_center, y_center, x2, y2):
            return True
        if x1 <= x_center <= x2:
            if y1 <= y_center <= y2: return True
            if abs(y1-y_center)<= radius or abs(y2-y_center)<=radius:
                return True
        if y1 <= y_center <= y2:
            if abs(x1-x_center)<= radius or abs(x2-x_center)<=radius:
                return True
        return False

s = Solution()
radius = 1; x_center = 0; y_center = 0; x1 = 1; y1 = -1; x2 = 3; y2 = 1
radius = 1; x_center = 1; y_center = 1; x1 = 1; y1 = -3; x2 = 2; y2 = -1
print(s.checkOverlap(radius, x_center, y_center, x1, y1, x2, y2))

