class Solution(object):
    def canVisitAllRoomsi_helper_dfs(self, rooms, visited, start):
        for r in rooms[start]:
            if visited[r] != 0: continue
            visited[r] = 1
            self.canVisitAllRoomsi_helper_dfs(rooms, visited, r)

    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        size = len(rooms)
        visited = [0] * size
        start = 0
        visited[0] = 1
        self.canVisitAllRoomsi_helper_dfs(rooms, visited, start)
        for i in range(size):
            if not visited[i]:
                return False
        return True

    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = len(grid)
        if m <= 0: return -1
        n = len(grid[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
        max_dist = -1
        while len(queue) > 0:
            i, j, dist = queue.pop(0)
            max_dist = max(max_dist, dist)
            for direct in directions:
                ni = i + direct[0]
                nj = j + direct[1]
                if ni<0 or nj<0 or ni>=m or nj>=n: continue
                if grid[ni][nj] != 0: continue
                grid[ni][nj] = -1
                queue.append((ni, nj, dist+1))
        return max_dist


if __name__ == "__main__":
    s = Solution()

    grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]] # 2
    grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]] # 4
    res = s.maxDistance(grid)
    print("distance:", res)
    '''
    rooms = [[1],[2],[3],[]]
    rooms = [[1,3],[3,0,1],[2],[0]]
    res = s.canVisitAllRooms(rooms)
    print("rooms:", res)
    '''
