"""
"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        node_map = {}
        queue = []
        queue.append(node)
        while len(queue) > 0:
            node = queue[0]
            queue.pop(0)
            new_node = UndirectedGraphNode(node.label)
            node_map[node] = new_node
            for cur in node.neighbors:
                if cur not in node_map:
                    queue.append(cur)
        for node in node_map.keys():
            new_node = node_map[node]
            for cur in node.neighbors:
                new_node.neighbors.append(node_map[cur])
        return node_map[node]
    
s = Solution()
node = UndirectedGraphNode()
print(s.cloneGraph(node))
