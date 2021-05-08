class Solution(object):

    def helper(self, graph, color, idx, colors):
        if colors[idx] != 0:
            return colors[idx] == color
        colors[idx] = color
        for node in graph[idx]:
            if not self.helper(graph, -color, node, colors):
                return False
        return True

    def isBipartite_DFS(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        colors = [0] * n
        for i in range(n):
            if colors[i] == 0:
                if not self.helper(graph, 1, i, colors):
                    return False
        return True

    def isBipartite(self, graph):
        n = len(graph)
        colors = [0] * n
        for i in range(n):
            if colors[i] != 0: continue
            queue = [i]
            colors[i] = 1
            while len(queue) > 0:
                top = queue[0]; queue.pop(0)
                for node in graph[top]:
                    if colors[node] == colors[top]: return False
                    elif colors[node] == 0:
                        queue.append(node)
                        colors[node] = -1 * colors[top]
        return True




s = Solution()
graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
graph = [[1,3], [0,2], [1,3], [0,2]]
print(s.isBipartite(graph))

