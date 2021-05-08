class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m <=0: return 0
        n = len(grid[0])
        level = 0
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
        directs = [[0,-1], [0,1], [-1,0], [1,0]]
        while len(queue):
            level += 1
            qlen = len(queue)
            print(level, queue)
            for i in range(qlen):
                x, y = queue[0]; queue.pop(0)
                for direct in directs:
                    nx = x + direct[0]
                    ny = y + direct[1]
                    if nx<0 or ny<0 or nx>=m or ny>=n: continue
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append([nx, ny])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: return -1
        return level-1

s = Solution()
grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[0,2]]
print(s.orangesRotting(grid))

