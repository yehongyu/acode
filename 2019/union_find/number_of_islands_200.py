#coding=utf-8

class Solution(object):
    def numIslands_with_dfs(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    res += 1
        return res

    def dfs(self, grid, r, c):
        steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        grid[r][c] = '0'
        for i, j in steps:
            nr = r + i; nc = c + j
            if nr >=0 and nr < len(grid) and nc >=0 and nc < len(grid[0]):
                if grid[nr][nc] == '1':
                    self.dfs(grid, nr, nc)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        M = len(grid)
        if M == 0:
            return 0
        N = len(grid[0])
        queue = []
        steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for r in range(M):
            for c in range(N):
                if grid[r][c] == '1':
                    res += 1
                    queue.append([r, c])
                    while len(queue) > 0:
                        cur_i, cur_j = queue[0]
                        queue = queue[1:]
                        grid[cur_i][cur_j] = '0'
                        for delta_i, delta_j in steps:
                            nr = cur_i + delta_i; nc = cur_j + delta_j
                            if nr >= 0 and nr < M and nc >= 0 and nc < N and grid[nr][nc] == '1':
                                queue.append([nr, nc])
        return res


s = Solution()

grid = [
["1","1", "1", "1", "0"],
["1", "1", "0", "1", "0"],
["1", "1", "0", "0", "0"],
["0", "0", "0", "0", "0"],
]
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(s.numIslands(grid))
