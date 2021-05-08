#coding=utf-8

class MyCalendarThree(object):

    def __init__(self):
        self.map = {}

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        if start not in self.map:
            self.map[start] = 0
        self.map[start] += 1
        if end not in self.map:
            self.map[end] = 0
        self.map[end] -= 1
        res = 0
        cur_count = 0
        for key in sorted(self.map.keys()):
            cur_count += self.map[key]
            res = max(res, cur_count)
        print(self.map)
        return res


# Your MyCalendarThree object will be instantiated and called as such:
obj = MyCalendarThree()
print(obj.book(24, 40))
print(obj.book(43, 50))
print(obj.book(27, 43))
'''
print(obj.book(5, 21))
print(obj.book(30, 40))
print(obj.book(14, 29))
print(obj.book(3, 19))
print(obj.book(3, 14))
print(obj.book(25, 39))
print(obj.book(6, 19))
'''
'''
print(obj.book(10, 20))
print(obj.book(50, 60))
print(obj.book(10, 40))
print(obj.book(5, 15))
print(obj.book(5, 10))
print(obj.book(25, 55))
'''

