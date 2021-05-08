class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n <= 1: return
        mid = n // 2
        for i in range(mid):
            for j in range(i, n-i-1):
                tmp = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[i][j]
                matrix[i][j] = tmp

    def transpose(self, matrix):
        m = len(matrix)
        if m <=0: return []
        n = len(matrix[0])
        res = []
        for j in range(n):
            tmp = []
            for i in range(m):
                tmp.append(matrix[i][j])
            res.append(tmp[0:])
        return res

s = Solution()
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
s.rotate(matrix)
print(matrix)

print(s.transpose(matrix))

