#coding=utf-8

class Solution(object):
    def solve_with_dfs(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        M = len(board)
        if M <= 0:
            return
        N = len(board[0])
        edges = []
        for i in range(M):
            edges.append([i, 0])
            edges.append([i, N-1])
        for j in range(1, N-1):
            edges.append([0, j])
            edges.append([M-1, j])
        for edge in edges:
            if board[edge[0]][edge[1]] == 'O':
                self.dfs(board, edge[0], edge[1])

        for i in range(M):
            for j in range(N):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
        return board


    def dfs(self, board, r, c):
        board[r][c] = '#'
        steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i, j in steps:
            nr = r + i; nc = c + j
            if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]):
                if board[nr][nc] == 'O':
                    self.dfs(board, nr, nc)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m <= 0:
            return board
        n = len(board[0])
        edges = []
        for i in range(m):
            edges.append([i, 0])
            edges.append([i, n-1])
        for j in range(1, n-1):
            edges.append([0, j])
            edges.append([m-1, j])
        steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        queue = []
        for r, c in edges:
            if board[r][c] == 'O':
                queue.append([r, c])
                while len(queue) > 0:
                    cur_r, cur_c = queue[0]
                    board[cur_r][cur_c] = '#'
                    queue = queue[1:]
                    for d_r, d_c in steps:
                        nr = cur_r + d_r; nc = cur_c + d_c
                        if nr >= 0 and nr < m and nc >= 0 and nc < n and board[nr][nc] == 'O':
                            queue.append([nr, nc])

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
        return board





s = Solution()
board = [
["X", "X", "X", "X"],
["X", "O", "O", "X"],
["X", "X", "O", "X"],
["X", "O", "X", "X"]]
print(s.solve(board))


