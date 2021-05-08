#coding=utf-8

class RangeModule(object):

    def __init__(self):
        self.segments = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        i = 0
        while i < len(self.segments) and self.segments[i][0] < left:
            i += 1
        self.segments.insert(i, [left, right])
        res = []
        for i in range(len(self.segments)):
            if len(res) == 0:
                res.append(self.segments[i])
                continue
            start = self.segments[i][0]
            if start > res[-1][1]:
                res.append(self.segments[i])
            else:
                res[-1][1] = max(self.segments[i][1], res[-1][1])
        self.segments = res[0:]
        print(self.segments)

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        if len(self.segments) == 0 or left < self.segments[0][0]:
            return False
        start = 0; end = len(self.segments)-1
        while start < end:
            mid = start + (end - start + 1) / 2
            if self.segments[mid][0] > left:
                end = mid - 1
            else:
                start = mid
        return self.segments[start][1] >= right


    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        res = []
        for i in range(len(self.segments)):
            start = self.segments[i][0]
            end = self.segments[i][1]
            if start > right or end < left:
                res.append(self.segments[i])
            else:
                if start < left:
                    res.append([start, left])
                if end > right:
                    res.append([right, end])
        self.segments = res[0:]
        print(self.segments)


# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
obj.addRange(10, 20)
#print(obj.queryRange(10, 14))
#print(obj.queryRange(13, 15))
#print(obj.queryRange(16, 17))
obj.removeRange(14, 16)
print(obj.queryRange(10, 14))
print(obj.queryRange(13, 15))
print(obj.queryRange(16, 17))


