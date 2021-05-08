#coding=utf-8

class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        if n <= 0:
            return 0
        if SVNRepo.isBadVersion(1):
            return 1
        if n == 1:
            return 1
        start = 1; end = n
        while start + 1 < end:
            mid = start + (end-start)/2
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid
        if SVNRepo.isBadVersion(start):
            return start
        else:
            return end

