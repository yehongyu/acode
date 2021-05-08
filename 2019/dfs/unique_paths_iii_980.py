class Solution(object):
    def dfs(self, grid, res, x, y, cnt):
        m = len(grid)
        n = len(grid[0])
        directs = [[-1,0],[1,0],[0,-1],[0,1]]
        for direct in directs:
            nx = x + direct[0]
            ny = y + direct[1]
            if nx<0 or nx>=m or ny<0 or ny>=n: continue
            if cnt == 0 and grid[nx][ny] == 2:
                res[0] += 1
                continue
            if grid[nx][ny] == 0:
                cnt -= 1
                grid[nx][ny] = -1
                self.dfs(grid, res, nx, ny, cnt)
                grid[nx][ny] = 0
                cnt += 1

    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m <= 0: return 0
        n = len(grid[0])
        start = []; zero_cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: zero_cnt += 1
                elif grid[i][j] == 1: start = [i, j]
        res = [0]
        self.dfs(grid, res, start[0], start[1], zero_cnt)
        return res[0]

s = Solution()
grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]

grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
print(s.uniquePathsIII(grid))