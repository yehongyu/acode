#coding=utf-8

class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        m = len(matrix)
        if m <= 0:
            return 0
        n = len(matrix[0])
        if n <= 0:
            return 0
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return 0
        i = m - 1; j = 0
        cnt = 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                i -= 1; j += 1
                cnt += 1
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return cnt

s = Solution()
matrix = [[3, 4]]
print(s.searchMatrix(matrix, 3))
print(s.searchMatrix(matrix, 6))
matrix = [
      [1, 3, 5, 7],
      [2, 4, 7, 8],
      [3, 5, 9, 10]
    ]
print(s.searchMatrix(matrix, 3))
print(s.searchMatrix(matrix, 7))
print(s.searchMatrix(matrix, 11))
print(s.searchMatrix(matrix, 4))

