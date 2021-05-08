class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal <= 0 or maxChoosableInteger <= 0: return False
        sum_val = sum([i for i in range(1, maxChoosableInteger + 1)])
        if desiredTotal > sum_val: return False
        if desiredTotal <= maxChoosableInteger: return True
        visited = set()
        vi

