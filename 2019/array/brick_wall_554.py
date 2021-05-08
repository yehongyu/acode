class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        map = {}
        n = len(wall)
        for i in range(n):
            acc = 0
            for j in range(len(wall[i])-1):
                acc += wall[i][j]
                if acc not in map: map[acc] = 0
                map[acc] += 1
        cnt = 0;
        print(map)
        for acc in map.keys():
            if map[acc] > cnt:
                cnt = map[acc]
        return n-cnt

s = Solution()
wall = [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]
wall = [[1,1],[2],[1,1]]
print(s.leastBricks(wall))
