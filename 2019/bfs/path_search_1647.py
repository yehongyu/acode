class Solution:
    """
    @param n: The number of points
    @param G: The description of graph
    @param S: The point S
    @param T: The point T
    @return: output all the paths from S to T
    """
    def dfs(self, graph, visited, res, path, S, T):
        visited[S] = 1
        if S == T:
            res.append(path[0:])
        if S in graph:
            nodes = sorted(graph[S])
            for nn in nodes:
                if visited[nn] != 1:
                    path.append(nn)
                    self.dfs(graph, visited, res, path, nn, T)
                    path.pop(-1)
        visited[S] = -1

    def getPath_dfs(self, n, G, S, T):
        # Write your code here
        graph = {}
        for edge in G:
            s, e = edge
            if s not in graph: graph[s] = []
            if e not in graph: graph[e] = []
            graph[s].append(e)
            graph[e].append(s)
        visited = [0]*n
        res = []
        path = [S]
        self.dfs(graph, visited, res, path, S, T)
        return res

    def getPath_dfs(self, n, G, S, T):
        # Write your code here
        graph = {}
        for edge in G:
            s, e = edge
            if s not in graph: graph[s] = []
            if e not in graph: graph[e] = []
            graph[s].append(e)
            graph[e].append(s)
        visited = [0]*n
        res = []
        path = [S]
        self.dfs(graph, visited, res, path, S, T)
        return res

s = Solution()
n = 4
G = [[0,1],[0,2],[1,2],[1,3],[3,2]]
S = 0
T = 2
print(s.getPath(n, G, S, T))
