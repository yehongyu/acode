class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    def isValid(self, path, pos):
        size = len(path)
        for row in range(size):
            if path[row] == pos:
                return False
            if row + path[row] == size + pos:
                return False
            if abs(row-size) == abs(path[row]-pos):
                return False
        return True

    def helper(self, res, path, n):
        if len(path) == n:
            res.append(path[0:])
            return
        for i in range(0, n):
            if self.isValid(path, i):
                path.append(i)
                self.helper(res, path, n)
                path.pop(-1)


    def solveNQueens(self, n):
        # write your code here
        res = []
        path = []
        self.helper(res, path, n)
        print(res)
        return len(res)

s = Solution()
print(s.solveNQueens(4))