
"""
Definition for a point.
"""
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        if grid[i][j] != 1:
            return
        grid[i][j] = 9
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for direction in directions:
            nx = i + direction[0]
            ny = j + direction[1]
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                self.dfs(grid, nx, ny)

    def numIslands_DFS(self, grid):
        # write your code here
        m = len(grid)
        if m <= 0: return 0
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    res += 1
        return res

    def numIslands(self, grid):
        m = len(grid)
        if m <= 0: return 0
        n = len(grid[0])
        res = 0
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1
                    queue = [[i, j]]
                    while len(queue) > 0:
                        x, y = queue[0]; queue.pop(0)
                        grid[x][y] = 9
                        for direction in directions:
                            nx = x + direction[0]
                            ny = y + direction[1]
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                                queue.append([nx, ny])
        return res


    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def findFather(self, father, x):
        if x not in father:
            father[x] = x
            return x
        tmp = x
        while tmp != father[tmp]:
            tmp = father[tmp]

        return tmp

    def numIslands2(self, m, n, operators):
        # write your code here
        if m <= 0 or n <= 0: return []
        father = {}
        res = []
        cnt = 0
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for op in operators:
            p = op.x * n + op.y
            if p not in father:
                fp = self.findFather(father, p)
                if fp == p: cnt += 1
                for direction in directions:
                    nx = op.x + direction[0]
                    ny = op.y + direction[1]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                    q = nx * n + ny
                    if q not in father: continue
                    fq = self.findFather(father, q)
                    if fq != fp:
                        father[fq] = fp
                        cnt -= 1
            res.append(cnt)
        return res

s = Solution()
m = 4; n = 5
A = [Point(1,1),Point(0,1), Point(3,3), Point(3,4)]
m = 2; n = 2
A = [Point(0,0),Point(1,1), Point(1,0), Point(0,1)]
m = 3; n = 3
A = [Point(0,0),Point(0,1), Point(2,2), Point(2,2)]
print(s.numIslands2(m, n, A))



s = Solution()
grid = [
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
print(s.numIslands(grid))
