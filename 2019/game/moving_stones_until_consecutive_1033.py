#coding=utf-8

class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        tmps = [a, b, c]
        a, b, c = sorted(tmps)
        if b-a == 1 and c-b == 1:
            return [0, 0]
        minstep = 2
        if b-a == 1 or b-a == 2 or c-b == 1 or c-b == 2:
            minstep = 1
        maxstep = c - a - 2
        return [minstep, maxstep]


s = Solution()
print(s.numMovesStones(1, 2, 3))
print(s.numMovesStones(1, 2, 5))
print(s.numMovesStones(4, 3, 2))
print(s.numMovesStones(3, 5, 1))
