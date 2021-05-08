import sys
class Solution:
    """
    @param matrix: a matrix
    @return: the minimum height
    """
    def dfs(self, matrix, dist, x, y):
        m = len(matrix)
        n = len(matrix[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
            cur_val = dist[x][y] + matrix[nx][ny]
            if dist[nx][ny] > cur_val:
                dist[nx][ny] = cur_val
                self.dfs(matrix, dist, nx, ny)

    def minPathSumII_dfs(self, matrix):
        # Write your code here
        m = len(matrix)
        if m <= 0: return -1
        n = len(matrix[0])
        dist = []
        for i in range(m):
            dist.append([sys.maxsize] * n)
        dist[m-1][0] = matrix[m-1][0]
        self.dfs(matrix, dist, m-1, 0)
        return dist[0][n-1]

    def bfs(self, matrix, dist, x, y):
        m = len(matrix)
        n = len(matrix[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = [[x, y]]
        while len(queue) > 0:
            i, j = queue[0]; queue.pop(0)
            print(i, j)
            for direction in directions:
                nx = i + direction[0]
                ny = j + direction[1]
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                cur_val = dist[i][j] + matrix[nx][ny]
                if dist[nx][ny] > cur_val:
                    dist[nx][ny] = cur_val
                    queue.append([nx, ny])

    def minPathSumII(self, matrix):
        # Write your code here
        m = len(matrix)
        if m <= 0: return -1
        n = len(matrix[0])
        dist = []
        for i in range(m):
            dist.append([sys.maxsize] * n)
        dist[m-1][0] = matrix[m-1][0]
        self.bfs(matrix, dist, m-1, 0)
        return dist[0][n-1]

s = Solution()
matrix = [[1,1,1],[1,1,1],[1,1,1]]
matrix = [[2,3],[3,2]]
matrix = [[6,5,3,3,7,9,6,8,1,4,8,3],[7,6,6,9,8,6,7,5,3,0,9,8],[7,0,6,9,9,0,3,7,7,9,1,7],[8,9,5,2,3,5,5,2,2,2,3,2]]
print(s.minPathSumII(matrix))


