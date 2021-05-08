class Trie():
    def __init__(self):
        self.is_word = False
        self.child = [None] * 26

class Solution(object):
    def dfs(self, board, root, x, y, path, res):
        print(x, y, path)
        if root.is_word:
            res.add(''.join(path))
        m = len(board)
        n = len(board[0])
        directs = [[0,-1],[0,1],[-1,0],[1,0]]
        for direct in directs:
            nx = x + direct[0]
            ny = y + direct[1]
            if nx<0 or nx>=m or ny<0 or ny>=n: continue
            print('direct', nx, ny, board[nx][ny])
            ch = board[nx][ny]
            idx = ord(ch)-ord('a')
            if ch == '#': continue
            if not root.child[idx]: continue
            board[nx][ny] = '#'
            path.append(ch)
            self.dfs(board, root.child[idx], nx, ny, path, res)
            path.pop(-1)
            board[nx][ny] = ch

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m = len(board)
        if m <= 0: return False
        n = len(board[0])
        root = Trie()
        for word in words:
            cur = root
            for ch in word:
                idx = ord(ch)-ord('a')
                if not cur.child[idx]:
                    cur.child[idx] = Trie()
                cur = cur.child[idx]
            cur.is_word = True
        res = set()
        for i in range(m):
            for j in range(n):
                ch = board[i][j]
                idx = ord(ch) - ord('a')
                print(i, j, ch)
                if root.child[idx]:
                    board[i][j] = '#'
                    path = [ch]
                    self.dfs(board, root.child[idx], i, j, path, res)
                    board[i][j] = ch
        return list(res)


s = Solution()
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
board = [["a","a"]]
words = ["aa"]
board = [["a","b"]]
words = ["ba"]
board = [["a","a"]]
words = ["a"]
print(s.findWords(board, words))

