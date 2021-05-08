from functools import cmp_to_key
def cmp(x, y):
    if x[0] != y[0]: return x[0]-y[0]
    else: return x[1]-y[1]

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)
        if n <= 1: return 0
        res = 0
        intervals = sorted(intervals, key=cmp_to_key(cmp))
        last_end = intervals[0][1]
        for i in range(1, n):
            print(i, intervals[i], last_end, res)
            if intervals[i][0] < last_end:
                res += 1
                last_end = min(last_end, intervals[i][1])
            else:
                last_end = intervals[i][1]
        return res

s = Solution()
intervals = [[1,2],[2,3]]
intervals = [[1,2],[1,2],[1,2]]
intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
print(s.eraseOverlapIntervals(intervals))
