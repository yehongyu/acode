class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        directs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        m = len(board)
        if m == 0: return
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                live_cnt = 0
                for direct in directs:
                    nx = i + direct[0]
                    ny = j + direct[1]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                    if board[nx][ny] % 2 == 1:
                        live_cnt += 1
                if board[i][j] == 1 and (live_cnt < 2 or live_cnt > 3):
                    board[i][j] = 3
                elif board[i][j] == 0 and live_cnt == 3:
                    board[i][j] = 2
                print(i, j, board[i][j])
        for i in range(m):
            for j in range(n):
                if board[i][j] in [1,2]:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

s = Solution()
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
s.gameOfLife(board)
print(board)
