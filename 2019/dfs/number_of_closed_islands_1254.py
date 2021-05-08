class Solution(object):

    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        directs = [[0,-1], [0,1], [-1,0], [1,0]]
        flag = True
        for direct in directs:
            nx = i + direct[0]
            ny = j + direct[1]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                flag = False
                continue
            if grid[nx][ny] in [1,2]: continue
            if grid[nx][ny] == 0:
                grid[nx][ny] = 2
                if not self.dfs(grid, nx, ny): flag = False
        return flag

    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m <= 0: return 0
        n = len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j] = 2
                    if self.dfs(grid, i, j):
                        cnt += 1
        return cnt

s = Solution()
grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
print(s.closedIsland(grid))
