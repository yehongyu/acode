class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n <= 0: return [newInterval]
        res = []
        i = 0
        while i < n and intervals[i][0] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        if len(res) > 0:
            if newInterval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], newInterval[1])
            else:
                res.append(newInterval)
        else:
            res.append(newInterval)
        while i < n:
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][0] = min(res[-1][0], intervals[i][0])
                res[-1][1] = max(res[-1][1], intervals[i][1])
            i += 1
        return res

s = Solution()
intervals = [[1,3],[6,9]]; newInterval = [2,5]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]; newInterval = [4,8]
print(s.insert(intervals, newInterval))
