#coding=utf-8

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        self.rows = rows
        self.cols = cols
        self.sums = []
        for i in range(rows+1):
            self.sums.append([0]*(cols+1))
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                self.sums[i][j] = self.sums[i][j-1] + matrix[i-1][j-1] + \
                                      self.sums[i-1][j] - self.sums[i-1][j-1]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sums[row2+1][col2+1] - self.sums[row2+1][col1] - self.sums[row1][col2+1] + self.sums[row1][col1]

if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    matrix = [[-1, -2, -9, 6], [8, -9, -3, -6], [2, 9, -7, -6]]
    nm = NumMatrix(matrix)
    print nm.sumRegion(2, 1, 2, 1)
    print nm.sumRegion(2, 1, 2, 2)
    print nm.sumRegion(2, 2, 2, 2)
    print nm.sumRegion(1, 3, 2, 3)
    print nm.sumRegion(1, 3, 2, 3)
