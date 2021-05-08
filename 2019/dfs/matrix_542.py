class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        if m <=0: return matrix
        n = len(matrix[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append([i, j])
        level = 0
        directs = [[0,-1], [0,1], [-1,0], [1,0]]
        while len(queue)>0:
            qlen = len(queue)
            level += 1
            for i in range(qlen):
                x, y = queue[0]; queue.pop(0)
                for direct in directs:
                    nx = x + direct[0]
                    ny = y + direct[1]
                    if nx<0 or ny<0 or nx>=m or ny>=n: continue
                    if matrix[nx][ny] == 1:
                        matrix[nx][ny] = -level
                        queue.append([nx, ny])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] < 0:
                    matrix[i][j] = -matrix[i][j]
        return matrix


s = Solution()
matrix = [[0,0,0],
 [0,1,0],
 [1,1,1]]
print(s.updateMatrix(matrix))
