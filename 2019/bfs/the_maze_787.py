import sys

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def dfs(self, maze, visited, start, destination):
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for direction in directions:
            nx = start[0]
            ny = start[1]
            while maze[nx][ny] != 1:
                nx += direction[0]
                ny += direction[1]
            nx -= direction[0]
            ny -= direction[1]
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                print(nx, ny)
                if destination[0] == nx and destination[1] == ny:
                    return True
                if self.dfs(maze, visited, [nx, ny], destination):
                    return True
        return False

    def bfs(self, maze, visited, start, destination):
        queue = []
        queue.append(start)
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while len(queue) > 0:
            node = queue[0]; queue.pop(0)
            for direction in directions:
                nx = node[0]
                ny = node[1]
                while maze[nx][ny] != 1:
                    nx += direction[0]
                    ny += direction[1]
                nx -= direction[0]
                ny -= direction[1]
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    print(nx, ny)
                    if destination[0] == nx and destination[1] == ny:
                        return True
                    queue.append([nx, ny])
        return False


    def hasPath(self, maze, start, destination):
        # write your code here
        m = len(maze)
        n = len(maze[0])
        maze.insert(0, [1]*n)
        maze.append([1]*n)
        for i in range(m+2):
            maze[i].insert(0, 1)
            maze[i].append(1)
        visited = []
        for i in range(m+2):
            visited.append([0] * (n+2))
        start = [start[0]+1, start[1]+1]
        destination = [destination[0]+1, destination[1]+1]
        visited[start[0]][start[1]] = 1
        #return self.dfs(maze, visited, start, destination)
        return self.bfs(maze, visited, start, destination)

    def dfs_dist(self, maze, dists, start, destination):
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for direction in directions:
            nx = start[0]
            ny = start[1]
            while maze[nx][ny] != 1:
                nx += direction[0]
                ny += direction[1]
            nx -= direction[0]
            ny -= direction[1]
            delte_d = abs(nx - start[0]) + abs(ny - start[1])
            cur_dist = dists[start[0]][start[1]] + delte_d
            if dists[nx][ny] > cur_dist:
                dists[nx][ny] = cur_dist
                self.dfs_dist(maze, dists, [nx, ny], destination)

    def bfs_dist(self, maze, dists, start, destination):
        queue = []
        queue.append(start)
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while len(queue) > 0:
            node = queue[0]; queue.pop(0)
            for direction in directions:
                nx = node[0]
                ny = node[1]
                while maze[nx][ny] != 1:
                    nx += direction[0]
                    ny += direction[1]
                nx -= direction[0]
                ny -= direction[1]
                delte_d = abs(nx - node[0]) + abs(ny - node[1])
                cur_dist = dists[node[0]][node[1]] + delte_d
                if dists[nx][ny] > cur_dist:
                    dists[nx][ny] = cur_dist
                    queue.append([nx, ny])

    def shortestDistance(self, maze, start, destination):
        m = len(maze)
        n = len(maze[0])
        maze.insert(0, [1]*n)
        maze.append([1]*n)
        for i in range(m+2):
            maze[i].insert(0, 1)
            maze[i].append(1)
        dists = []
        for i in range(m+2):
            dists.append([sys.maxsize] * (n+2))
        start = [start[0]+1, start[1]+1]
        destination = [destination[0]+1, destination[1]+1]
        dists[start[0]][start[1]] = 0
        #self.dfs_dist(maze, dists, start, destination)
        self.bfs_dist(maze, dists, start, destination)
        res = dists[destination[0]][destination[1]]
        return res if res < sys.maxsize else -1

    def dfs_dist_hole(self, res, maze, dists, path, start, destination):
        directions = [[-1, 0, 'u'], [1, 0, 'd'], [0, -1, 'l'], [0, 1, 'r']]
        for direction in directions:
            path.append(direction[2])
            nx = start[0]
            ny = start[1]
            while maze[nx][ny] != 1:
                nx += direction[0]
                ny += direction[1]
            nx -= direction[0]
            ny -= direction[1]

            flag = False
            delte_d = abs(nx - start[0]) + abs(ny - start[1])
            cur_dist = dists[start[0]][start[1]] + delte_d
            if dists[nx][ny] > cur_dist:
                flag = True

            if direction[0] == 0:
                for j in range(start[1]+1, ny+1):
                    cur_dist = dists[start[0]][start[1]]+j-start[1]
                    if nx == destination[0] and j == destination[1]:
                        if cur_dist < dists[nx][j]:
                            res[-1] = path[0:]
                    dists[nx][j] = min(dists[nx][j], cur_dist)
            else:
                for i in range(start[0]+1, nx+1):
                    cur_dist = dists[start[0]][start[1]]+i-start[0]
                    if i == destination[0] and ny == destination[1]:
                        if cur_dist < dists[i][ny]:
                            res[-1] = path[0:]
                    dists[i][ny] = min(dists[i][ny], cur_dist)
            if flag:
                self.dfs_dist_hole(res, maze, dists, path, [nx, ny], destination)
            path.pop(-1)

    ## wrong
    def findShortestWay(self, maze, ball, hole):
        m = len(maze)
        n = len(maze[0])
        maze.insert(0, [1]*n)
        maze.append([1]*n)
        for i in range(m+2):
            maze[i].insert(0, 1)
            maze[i].append(1)
        dists = []
        for i in range(m+2):
            dists.append([sys.maxsize] * (n+2))
        start = [ball[0]+1, ball[1]+1]
        destination = [hole[0]+1, hole[1]+1]
        dists[start[0]][start[1]] = 0
        path = []
        res = [['impossible']]
        self.dfs_dist_hole(res, maze, dists, path, start, destination)
        return ''.join(res[0])

    def bfs_maps(self, maps, visited, start, end):
        m = len(maps)
        n = len(maps[0])
        queue = []
        queue.append([start[0], start[1], 0])
        visited[start[0]][start[1]] = 1
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while len(queue) > 0:
            x, y, dist = queue[0]; queue.pop(0)
            for direction in directions:
                nx = x + direction[0]
                ny = y + direction[1]
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                if nx == end[0] and ny == end[1]:
                    return dist + 1
                if visited[nx][ny] == 0 and maps[nx][ny] == '.':
                    visited[nx][ny] = 1
                    queue.append([nx, ny, dist+1])
        return -1

    def theMazeIV(self, maps):
        m = len(maps)
        if m <= 0: return -1
        n = len(maps[0])
        start = None
        end = None
        visited = []
        for i in range(m):
            visited.append([0] * n)
            for j in range(n):
                if maps[i][j] == 'S': start = [i, j]
                if maps[i][j] == 'T': end = [i, j]
        if not start or not end: return -1
        return self.bfs_maps(maps, visited, start, end)






s = Solution()
maze = [
 [0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,1,0],
 [1,1,0,1,1],
 [0,0,0,0,0]
]
start = [0, 4]
end = [3, 2]
maze = [
    [0, 0, 1, 0, 0],
	[0, 0, 0, 0, 0],
	[0, 0, 0, 1, 0],
	[1, 1, 0, 1, 1],
	[0, 0, 0, 0, 0]
]
start = [0, 4]
end = [4, 4]
#print(s.hasPath(maze, start, end))
#print(s.shortestDistance(maze, start, end))
#print(s.findShortestWay(maze, start, end))

maps = [['S','.'],['#','T']]
maps = [".#.##.",".#S.#.",".#.###","..#.#.","......",".#T..."]
maps = [".S.##.T..","..##.#.#."]

print(s.theMazeIV(maps))
