"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from functools import cmp_to_key
def cmp(x, y):
    if x.start < y.start: return -1
    if x.start > y.startt: return 1
    if x.end < y.end: return -1
    if x.end > y.end: return -1
    return 0

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        n = len(intervals)
        if n <= 1: return True
        intervals = sorted(intervals, key=cmp_to_key(cmp))
        for i in range(1, n):
            if intervals[i-1].end > intervals[i].start:
                return False
        return True

    def minMeetingRooms(self, intervals):
        n = len(intervals)
        if n <= 1: return n
        n_map = {}
        for i in range(n):
            s = intervals[i].start
            e = intervals[i].end
            if s not in n_map:
                n_map[s] = 0
            if e not in n_map:
                n_map[e] = 0
            n_map[s] += 1
            n_map[e] -= 1
        res = 0
        rooms = 0
        keys = sorted(n_map.keys())
        for key in keys:
            rooms += n_map[key]
            res = max(res, rooms)
        return res

    def get_dist(self, x):
        x = sorted(x)
        l = 0
        r = len(x) - 1
        res = 0
        while l < r:
            res += x[r] - x[l]
            l += 1; r -= 1
        return res

    def minTotalDistance(self, grid):
        m = len(grid)
        if m <= 0: return 0
        n = len(grid[0])
        x = []
        y = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)
        return self.get_dist(x) + self.get_dist(y)


s = Solution()
intervals = []
print(s.canAttendMeetings(intervals))
