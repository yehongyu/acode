class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def dfs(self, grid, path, x0, y0, x, y):
        grid[x][y] = 9
        path.append('%s_%s' % (x-x0, y-y0))
        m = len(grid)
        n = len(grid[0])
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
            if grid[nx][ny] == 1:
                self.dfs(grid, path, x0, y0, nx, ny)

    def numberofDistinctIslands(self, grid):
        # write your code here
        m = len(grid)
        if m <= 0: return 0
        n = len(grid[0])
        res = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    self.dfs(grid, path, i, j, i, j)
                    if len(path) > 0:
                        res.add('*'.join(path))
        return len(res)

s = Solution()
grid = [
    [1,1,0,0,1],
    [1,0,0,0,0],
    [1,1,0,0,1],
    [0,1,0,1,1]
  ]
print(s.numberofDistinctIslands(grid))