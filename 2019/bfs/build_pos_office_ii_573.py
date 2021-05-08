import sys
class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def bfs(self, grid, visit_nums, dist, visited, i, j):
        m = len(grid)
        n = len(grid[0])
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        queue = [[i, j, 0]]
        while len(queue) > 0:
            x, y, cur_dist = queue[0]; queue.pop(0)
            for direction in directions:
                nx = x + direction[0]
                ny = y + direction[1]
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                if grid[nx][ny] == 0 and (nx * n + ny) not in visited:
                    visited.add(nx * n + ny)
                    visit_nums[nx][ny] += 1
                    dist[nx][ny] += cur_dist + 1
                    queue.append([nx, ny, cur_dist + 1])


    def shortestDistance(self, grid):
        # write your code here
        m = len(grid)
        if m <= 0: return -1
        n = len(grid[0])
        visit_nums = []
        dist = []
        for i in range(m):
            visit_nums.append([0] * n)
            dist.append([0] * n)
        house_num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    house_num += 1
                    visited = set()
                    self.bfs(grid, visit_nums, dist, visited, i, j)
                print(i, j, visit_nums)
        print(house_num)
        print(visit_nums)
        res = sys.maxsize
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and visit_nums[i][j] == house_num:
                    res = min(res, dist[i][j])
        return res


    def bfs2(self, grid, visit_nums, dist, visited, i, j):
        m = len(grid)
        n = len(grid[0])
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        queue = [[i, j, 0]]
        visited.add(i * n + j)
        visit_nums[i][j] += 1
        while len(queue) > 0:
            x, y, cur_dist = queue[0]; queue.pop(0)
            for direction in directions:
                nx = x + direction[0]
                ny = y + direction[1]
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                if (nx * n + ny) not in visited:
                    visited.add(nx * n + ny)
                    visit_nums[nx][ny] += 1
                    dist[nx][ny] += cur_dist + 1
                    queue.append([nx, ny, cur_dist + 1])


    def minTotalDistance_startfhome(self, grid):
        # write your code here
        m = len(grid)
        if m <= 0: return -1
        n = len(grid[0])
        visit_nums = []
        dist = []
        for i in range(m):
            visit_nums.append([0] * n)
            dist.append([0] * n)
        house_num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    house_num += 1
                    visited = set()
                    self.bfs2(grid, visit_nums, dist, visited, i, j)
                    print(i, j, visit_nums)
                    print(i, j, dist)
        print(house_num)
        print(visit_nums)
        res = sys.maxsize
        for i in range(m):
            for j in range(n):
                if visit_nums[i][j] == house_num:
                    res = min(res, dist[i][j])
        return res

    def bfs3(self, grid, visit_nums, dist, visited, x0, y0, i, j):
        m = len(grid)
        n = len(grid[0])
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        queue = [[i, j, 0]]
        visited.add(i * n + j)
        if grid[i][j] == 1:
            visit_nums[x0][y0] += 1
        while len(queue) > 0:
            x, y, cur_dist = queue[0]; queue.pop(0)
            for direction in directions:
                nx = x + direction[0]
                ny = y + direction[1]
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                if (nx * n + ny) not in visited:
                    visited.add(nx * n + ny)
                    if grid[nx][ny] == 1:
                        visit_nums[x0][y0] += 1
                        dist[x0][y0] += cur_dist + 1
                    queue.append([nx, ny, cur_dist + 1])


    def minTotalDistance(self, grid):
        # write your code here
        m = len(grid)
        if m <= 0: return -1
        n = len(grid[0])
        visit_nums = []
        dist = []
        for i in range(m):
            visit_nums.append([0] * n)
            dist.append([0] * n)
        house_num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    house_num += 1
                visited = set()
                self.bfs3(grid, visit_nums, dist, visited, i, j, i, j)
                print(i, j, visit_nums)
                print(i, j, dist)
        print(house_num)
        print(visit_nums)
        res = sys.maxsize
        for i in range(m):
            for j in range(n):
                if visit_nums[i][j] == house_num:
                    res = min(res, dist[i][j])
        return res






s = Solution()
grid = [[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]]
#print(s.shortestDistance(grid))
grid = [[1,1,0,0,1],[1,0,1,0,0],[0,0,1,0,1]]
#print(s.minTotalDistance(grid))
print(s.minTotalDistance_startfhome(grid))
