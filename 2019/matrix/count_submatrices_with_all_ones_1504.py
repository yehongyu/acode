# coding=utf-8

'''
First we'll find consecutive ones borizontally and then extends it to vertically.


'''
class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        if m <= 0: return 0
        n = len(mat[0])

        for i in range(m):
            for j in range(n):







