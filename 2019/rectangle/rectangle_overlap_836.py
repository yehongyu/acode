#coding=utf-8

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if rec2[0] >= rec1[2] or rec2[1] >= rec1[3] or \
            rec1[0] >= rec2[2] or rec1[1] >= rec2[3]:
            return False
        return True
s = Solution()
rec1 = [0,0,2,2]; rec2 = [1,1,3,3]
print(s.isRectangleOverlap(rec1, rec2))
rec1 = [0,0,1,1]; rec2 = [1,0,2,1]
print(s.isRectangleOverlap(rec1, rec2))


