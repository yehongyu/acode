class Solution(object):

    def dfs(self, grid, x, y):
        m = len(grid)
        n = len(grid[0])
        res = 1
        grid[x][y] = -1
        directs = [[0,1], [0,-1], [1,0], [-1,0]]
        for direct in directs:
            nx = x + direct[0]
            ny = y + direct[1]
            if nx<0 or ny<0 or nx>=m or ny>=n:continue
            if grid[nx][ny] != 1: continue
            res += self.dfs(grid, nx, ny)
        return res

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m <= 0: return 0
        n = len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1: continue
                grid[i][j] = -1
                area = self.dfs(grid, i, j)
                max_area = max(max_area, area)
        return max_area

if __name__ == "__main__":
    s = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    area = s.maxAreaOfIsland(grid)
    print("area:", area)