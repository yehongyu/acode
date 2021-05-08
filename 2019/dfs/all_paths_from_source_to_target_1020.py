class Solution:
    """
    @param graph: a 2D array
    @return: all possible paths from node 0 to node N-1
    """
    def helper(self, graph, res, path, visited, start, target):
        if start == target:
            res.append(path[0:])
        for next in graph[start]:
            if visited[next] == 0:
                path.append(next)
                visited[next] = 1
                self.helper(graph, res, path, visited, next, target)
                visited[next] = 0
                path.pop(-1)

    def allPathsSourceTarget_Visit(self, graph):
        # Write your code here
        n = len(graph)
        visited = [0] * n
        res = []
        path = [0]
        visited[0] = 1
        self.helper(graph, res, path, visited, 0, n-1)
        return res

    def helper_rec(self, graph, res, path, start, target):
        path.append(start)
        if start == target: res.append(path[0:])
        else:
            for next in graph[start]:
                self.helper_rec(graph, res, path, next, target)
        path.pop(-1)

    def allPathsSourceTarget(self, graph):
        n = len(graph)
        res = []
        path = []
        self.helper_rec(graph, res, path, 0, n-1)
        return res


s = Solution()
graph = [[1,2],[3],[3],[]]
res = s.allPathsSourceTarget(graph)
for l in res:
    print(l)
