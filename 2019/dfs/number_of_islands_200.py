class Solution(object):

    def dfs(self, grid, x, y):
        m = len(grid)
        n = len(grid[0])
        grid[x][y] = '2'
        directs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for direct in directs:
            nx = x + direct[0]
            ny = y + direct[1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
            if grid[nx][ny] == "1":
                self.dfs(grid, nx, ny)

    def bfs(self, grid, x, y):
        m = len(grid)
        n = len(grid[0])
        queue = [[x, y]]
        while len(queue) > 0:
            cur_x, cur_y = queue[0]; queue.pop(0)
            grid[cur_x][cur_y] = '2'
            directs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for direct in directs:
                nx = cur_x + direct[0]
                ny = cur_y + direct[1]
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                if grid[nx][ny] == "1":
                    queue.append([nx, ny])


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m <= 0: return 0
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    #self.dfs(grid, i, j)
                    self.dfs(grid, i, j)
        return res

s = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "1"],
]
print(s.numIslands(grid))