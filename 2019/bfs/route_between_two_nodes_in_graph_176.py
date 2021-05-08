"""
Definition for a Directed graph node
"""
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param: graph: A list of Directed graph node
    @param: s: the starting Directed graph node
    @param: t: the terminal Directed graph node
    @return: a boolean value
    """
    def hasRoute_BFS(self, graph, s, t):
        # write your code here
        n = len(graph)
        if n <= 0: return False
        if s == t: return True
        queue = [s]
        visited = {}
        while len(queue) > 0:
            node = queue[0]; queue.pop(0)
            if node == t: return True
            visited[node] = True
            for n_node in node.neighbors:
                if n_node not in visited or not visited[n_node]:
                    queue.append(n_node)
        return False

    def dfs(self, visited, s, t):
        if s == t: return True
        if s in visited:
            return False
        visited.add(s)
        res = False
        for next in s.neighbors:
            if next not in visited:
                res |= self.dfs(visited, next, t)
        return res

    def hasRoute_DFS(self, graph, s, t):
        n = len(graph)
        if n <= 0: return False
        if s == t: return True
        visited = set()
        return self.dfs(visited, s, t)


