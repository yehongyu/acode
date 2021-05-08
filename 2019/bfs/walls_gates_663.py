class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def bfs(self, rooms, visited, i, j):
        m = len(rooms)
        n = len(rooms[0])
        queue = [[i, j]]
        visited.add(i*n+j)
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        while len(queue) > 0:
            x, y = queue[0]; queue.pop(0)
            for direction in directions:
                nx = x + direction[0]
                ny = y + direction[1]
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                idx = nx * n + ny
                if idx in visited: continue
                visited.add(idx)
                if rooms[nx][ny] == -1: continue
                if rooms[nx][ny] == 0: continue
                rooms[nx][ny] = min(rooms[nx][ny], rooms[x][y]+1)
                queue.append([nx, ny])

    def wallsAndGates(self, rooms):
        # write your code here
        m = len(rooms)
        if m <= 0: return rooms
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    visited = set()
                    self.bfs(rooms, visited, i, j)
        return rooms

s = Solution()
rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
print(s.wallsAndGates(rooms))
