class Solution(object):
    def dfs(self, board, visited, word, x, y):
        print(x, y, word)
        if len(word) == 0: return True
        m = len(board)
        n = len(board[0])
        directs = [[0,-1],[0,1],[1,0],[-1,0]]
        for direct in directs:
            nx = x + direct[0]
            ny = y + direct[1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
            if nx * n + ny in visited: continue
            if board[nx][ny] == word[0]:
                visited.add(x*n+y)
                if self.dfs(board, visited, word[1:], nx, ny):
                    return True
                visited.remove(x*n+y)

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m <=0 or len(word) == 0: return False
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add(i*m+j)
                    if self.dfs(board, visited, word[1:], i, j):
                        return True
        return False

s = Solution()
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
word = "SEE"
word = "ABCB"
board = [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]]
word = "ABCESEEEFS"
print(s.exist(board, word))