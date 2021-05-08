class Solution:
    """
    @param map: the map
    @return: can you reach the endpoint
    """
    def reachEndpoint_BFS(self, map):
        # Write your code here
        m = len(map)
        if m <= 0: return False
        n = len(map[0])
        if map[0][0] == 9: return True
        if map[0][0] == 0: return False
        queue = []
        queue.append([0, 0])
        visited = []
        for i in range(m): visited.append([0] * n)
        visited[0][0] = 1

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while len(queue) > 0:
            x, y = queue[0]; queue.pop(0)
            for direction in directions:
                nx = x + direction[0]
                ny = y + direction[1]
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                if map[nx][ny] == 9: return True
                elif map[nx][ny] == 0: continue
                elif map[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
        return False

    def dfs(self, map, visited, x, y):
        print(x, y)
        m = len(map)
        n = len(map[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
            if map[nx][ny] == 9: return True
            elif map[nx][ny] == 0: continue
            elif map[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if self.dfs(map, visited, nx, ny):
                    return True
        return False

    def reachEndpoint(self, map):
        # Write your code here
        m = len(map)
        if m <= 0: return False
        n = len(map[0])
        if map[0][0] == 9: return True
        if map[0][0] == 0: return False
        visited = []
        for i in range(m): visited.append([0] * n)
        visited[0][0] = 1
        return self.dfs(map, visited, 0, 0)



s = Solution()
maps = [
	[1,1,1],
	[1,0,0],
	[1,0,9]
]
maps =[
    [1,1,1],
    [1,1,1],
    [1,1,9]
]
print(s.reachEndpoint(maps))


