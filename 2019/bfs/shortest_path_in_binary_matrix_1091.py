class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m <= 0: return -1
        n = len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1]: return -1
        queue = [[0,0]]
        level = 0
        directs = [[-1,0], [1,0],[0,-1],[0,1], [-1,1],[1,1],[-1,-1],[1,-1]]
        while len(queue) > 0:
            qlen = len(queue)
            level += 1
            for i in range(qlen):
                x, y = queue[0]; queue.pop(0)
                if x == m-1 and y == n-1: return level
                for direct in directs:
                    nx = x + direct[0]
                    ny = y + direct[1]
                    if nx<0 or nx>=m or ny<0 or ny>=n: continue
                    print(nx, ny)
                    if grid[nx][ny] == 1: continue
                    grid[nx][ny] = 1
                    queue.append([nx, ny])
        return -1

s = Solution()
grid = [[0,1],[1,0]]
grid = [[0,0,0],[1,1,0],[1,1,0]]
print(s.shortestPathBinaryMatrix(grid))

