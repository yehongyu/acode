class Solution(object):
    def isValidSudoku_array(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowflag = []
        colflag = []
        cellflag = []
        for i in range(9):
            rowflag.append([False] * 9)
            colflag.append([False] * 9)
            cellflag.append([False] * 9)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                idx = int(board[i][j])-1
                cell_idx = 3*(i // 3) + j // 3
                if rowflag[i][idx] or colflag[idx][j] or cellflag[cell_idx][idx]:
                    return False
                rowflag[i][idx] = True
                colflag[idx][j] = True
                cellflag[cell_idx][idx] = True
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        vals = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                row_val = str(i) + '(' + board[i][j] + ')'
                col_val = '(' + board[i][j] + ')' + str(j)
                cell_val = str(3*(i//3)) + '(' + board[i][j] + ')' + str(j//3)
                if row_val in vals or col_val in vals or cell_val in vals:
                    print(i, j, board[i][j], row_val, col_val, cell_val)
                    return False
                vals.add(row_val)
                vals.add(col_val)
                vals.add(cell_val)
        return True


s = Solution()
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(s.isValidSudoku(board))
