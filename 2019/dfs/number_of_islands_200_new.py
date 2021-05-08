class Solution(object):

    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        directs = [[-1,0], [1,0], [0,-1],[0,1]]
        for direct in directs:
            nx = i + direct[0]
            ny = j + direct[1]
            if nx<0 or nx>=m or ny<0 or ny>=n: continue
            if grid[nx][ny] != '1': continue
            grid[nx][ny] = '2'
            self.dfs(grid, nx, ny)


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m<=0: return 0
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '2'
                    self.dfs(grid, i, j)
                    res += 1
        return res

s = Solution()
grid = [
['1','1','0','1','0'],
['0','0','0','1','0'],
['1','1','0','0','0'],
['1','0','0','0','0'],]
print(s.numIslands(grid))
