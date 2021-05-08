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
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        res = []
        n = len(graph)
        if n <= 0:
            return res
        if n == 1:
            return [graph[0].label]
        inDegree = {}
        for node in graph:
            if node not in inDegree:
                inDegree[node] = 0
            else:
                for end in node.neighbors:
                    if end not in inDegree:
                        inDegree[end] = 0
                    inDegree[end] += 1
        queue = []
        for node in inDegree.keys():
            if inDegree[node] == 0:
                queue.append(node)
        while len(queue) > 0:
            node = queue[0]
            queue.pop(0)
            res.append(node.label)
            for cur in node.neighbors:
                inDegree[cur] -= 1
                if inDegree[cur] == 0:
                    queue.append(cur)
        return res




