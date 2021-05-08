#coding=utf-8

class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) <= 1:
            return len(intervals)
        inters = sorted(intervals, key=lambda x: (x[0], x[1]))
        print(inters)
        res = []
        res.append(inters[0])
        for i in range(1, len(inters)):
            if inters[i][1] > res[-1][1]:
                res.append(inters[i])
            print('res:', res)
        return len(res)

s = Solution()
nums = [[66672,75156],[59890,65654],[92950,95965],[9103,31953],[54869,69855],[33272,92693],[52631,65356],[43332,89722],[4218,57729],[20993,92876]]
print(s.removeCoveredIntervals(nums))

