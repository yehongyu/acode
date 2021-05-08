class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        n = len(coordinates)
        if n <= 1: return True
        dx = coordinates[1][0]-coordinates[0][0]
        dy = coordinates[1][1]-coordinates[0][1]
        for i in range(1,n):
            cur_dx = coordinates[i][0] - coordinates[0][0]
            cur_dy = coordinates[i][1] - coordinates[0][1]
            if cur_dy * dx != dy * cur_dx: return False
        return True


