class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m <= 0: return -1
        n = len(grid[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i, j])
        level = 0
        directs = [[-1,0], [1,0], [0,-1], [0,1]]
        while len(queue) > 0:
            qlen = len(queue)
            level += 1
            for i in range(qlen):
                x, y = queue[0]; queue.pop(0)
                for direct in directs:
                    nx = x + direct[0]
                    ny = y + direct[1]
                    if nx<0 or nx>=m or ny<0 or ny>=n: continue
                    if grid[nx][ny] == 1: continue
                    grid[nx][ny] = 1
                    queue.append([nx, ny])
        return level - 1 if level > 1 else -1

s = Solution()
grid = [[1,0,1],[0,0,0],[1,0,1]]
grid = [[1,0,0],[0,0,0],[0,0,0]]
print(s.maxDistance(grid))



