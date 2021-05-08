#coding=utf-8

class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end):
            return False
        size = len(start)
        i = 0
        j = 0
        while i < size or j < size:
            while (i < size and start[i] == 'X'): i += 1
            while (j < size and end[j] == 'X'): j += 1
            if i == size and j == size:
                return True
            if start[i] != end[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            i += 1
            j += 1
        return True



s = Solution()
print(s.canTransform('RXL', 'XRL'))
print(s.canTransform('RXL', 'RLX'))
print(s.canTransform('RXXLRXRXL', 'XRLXXRRLX'))
print(s.canTransform('RXL', 'RLXLL'))
#print(s.canTransform('R', 'L'))
