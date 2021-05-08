class Solution:
    """
    @param grid: a 2D grid
    @return: the minimize travel distance
    """
    def getDist(self, x):
        x = sorted(x)
        i = 0
        j = len(x) - 1
        res = 0
        while i < j:
            res += x[j] - x[i]
            j -= 1; i += 1
        return res

    def minTotalDistance(self, grid):
        m = len(grid)
        if m <= 0: return -1
        n = len(grid[0])
        x = []
        y = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)
        return self.getDist(x) + self.getDist(y)

s = Solution()
grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(s.minTotalDistance(grid))
