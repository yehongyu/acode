class Solution:
    """
    @param grid: a 2d boolean array
    @param k: an integer
    @return: the number of Islands
    """
    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        cnt = 1
        grid[i][j] = 9
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for direction in directions:
            nx = i + direction[0]
            ny = j + direction[1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
            if grid[nx][ny] != 1: continue
            cnt += self.dfs(grid, nx, ny)
        return cnt

    def numsofIsland_dfs(self, grid, k):
        # Write your code here
        m = len(grid)
        if m <= 0: return 0
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt = self.dfs(grid, i, j)
                    if cnt >= k:
                        res += 1
        return res

    def bfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        if grid[i][j] != 1: return 0
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        queue = [[i, j]]
        cnt = 0
        while len(queue) > 0:
            x, y = queue[0]; queue.pop(0)
            if grid[x][y] == 1: cnt += 1
            else: continue
            grid[x][y] = 9
            for direction in directions:
                nx = i + direction[0]
                ny = j + direction[1]
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                if grid[nx][ny] != 1: continue
                queue.append([nx, ny])
        return cnt

    def numsofIsland(self, grid, k):
        m = len(grid)
        if m <= 0: return 0
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt = self.bfs(grid, i, j)
                    if cnt >= k:
                        res += 1
        return res



s = Solution()
grid = [[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,1]]
k = 2
print(s.numsofIsland(grid, k))


