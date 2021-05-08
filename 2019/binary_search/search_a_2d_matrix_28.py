#coding=utf-8

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        m = len(matrix)
        if m <= 0:
            return False
        n = len(matrix[0])
        low = 0; high = m - 1
        while low + 1 < high:
            mid = low + (high-low)/2
            #print('mid:', mid, low, high)
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                low = mid
            else:
                high = mid
        if matrix[high][0] > target:
            pos = low
        else:
            pos = high
        #print('pos:', pos, low, high)
        left = 0; right = n - 1
        while left + 1 < right:
            mid = left + (right-left)/2
            if matrix[pos][mid] == target:
                return True
            elif matrix[pos][mid] < target:
                left = mid
            else:
                right = mid
        if matrix[pos][right] == target or matrix[pos][left] == target:
            return True
        return False

s = Solution()
#matrix = [[5]]
#print(s.searchMatrix(matrix, 2))
#print(s.searchMatrix(matrix, 5))
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
print(s.searchMatrix(matrix, 3))
print(s.searchMatrix(matrix, 50))
print(s.searchMatrix(matrix, 51))
print(s.searchMatrix(matrix, 1))
print(s.searchMatrix(matrix, 0))
