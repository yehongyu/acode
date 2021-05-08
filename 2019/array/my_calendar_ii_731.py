class MyCalendarTwo(object):

    def __init__(self):
        self.map ={}

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if start not in self.map: self.map[start] = 0
        if end not in self.map: self.map[end] = 0
        self.map[start] += 1
        self.map[end] -= 1
        cnt = 0
        keys = sorted(self.map.keys())
        for k in keys:
            cnt += self.map[k]
            if cnt >= 3:
                self.map[start] -= 1
                self.map[end] += 1
                return False
        return True
    
s =MyCalendarTwo()
print(s.book())

