class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def dfs(self, board, i, j):
        m = len(board)
        n = len(board[0])
        board[i][j] = '#'
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for direction in directions:
            nx = i + direction[0]
            ny = j + direction[1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
            if board[nx][ny] == 'O':
                self.dfs(board, nx, ny)

    def surroundedRegions(self, board):
        # write your code here
        m = len(board)
        if m <= 1: return board
        n = len(board[0])
        new_board = []
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(board[i][j])
            new_board.append(tmp[0:])
        print(new_board)
        for i in [0, m-1]:
            for j in range(n):
                if new_board[i][j] == 'O':
                    self.dfs(new_board, i, j)
        for j in [0, n-1]:
            for i in range(1, m-1):
                print(i, j, new_board[i][j])
                if new_board[i][j] == 'O':
                    self.dfs(new_board, i, j)
        print(new_board)
        for i in range(m):
            for j in range(n):
                if new_board[i][j] == 'O':
                    new_board[i][j] = 'X'
                elif new_board[i][j] == '#':
                    new_board[i][j] = 'O'
            board[i] = ''.join(new_board[i])
        return board

s = Solution()
board = ["XXXX","XOOX","XXOX","XOXX"]
board = ["XOXX","OXOX","XOXO","OXOX","XOXO","OXOX"]
print(s.surroundedRegions(board))
