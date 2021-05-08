'''
Constuct the graph with booth original edge and reverse edges,
but fllag the ddifferent edges.
Do a BFS start from node 0.

We create two lists of sets one for vertices indegree,
another for graph itself from the edges given.
We can have at most one outwards connection and many inwards,
so tracking visited edgeds here is being performed
by modifying these sets defined above saving a bit of space.

Starting from the node 0 we traverse the graph,
and count direct edges from explored vertices,
as they would have to be reversed in order for vertex 0
to be reachable from any node.

I choose BFS instead of DFS.
According to the restriction, the number of city could be
fifty thousand. I thought if I use DFS, it would be stack overflow.
It is a reason why I choose BFS.

We can use BFS to solve the problem, also we can use DFS.
First, I build indegree and outdegree based on connections.
indegree means node and its indegree nodes,
outdegree means node and its outdegree nodes.
I also use a visited set to record which node is visited already.
In my dfs function, we can traverse nerghborhood node through
indegree and outdegree, and if there is node in current start node's
outdegree, then I will add 1 to reorder_cnt.
It means this edge need to be reversed.
I also use a global variable to store the reorder_cnt.

'''

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) <= 0 or n<=1: return 0
        indegree = {}
        outdegree = {}
        for f, t in connections:
            if f not in outdegree: outdegree[f] = []
            if t not in indegree: indegree[t] = []
            outdegree[f].append(t)
            indegree[t].append(f)
        self.reorder_cnt = 0
        visited = set()
        visited.add(0)
        self.dfs(indegree, outdegree, visited, 0)
        #self.bfs(indegree, outdegree, visited, 0)
        return self.reorder_cnt

    def dfs(self, indegree, outdegree, visited, start):
        if start in indegree:
            for innode in indegree[start]:
                if innode not in visited:
                    visited.add(innode)
                    self.dfs(indegree, outdegree, visited, innode)
        if start in outdegree:
            for outnode in outdegree[start]:
                if outnode not in visited:
                    self.reorder_cnt += 1
                    visited.add(outnode)
                    self.dfs(indegree, outdegree, visited, outnode)


    def bfs(self, indegree, outdegree, visited, start):
        queue = [start]
        while len(queue) > 0:
            cur = queue[0]; queue.pop(0)
            if cur in indegree:
                for innode in indegree[cur]:
                    if innode not in visited:
                        visited.add(innode)
                        queue.append(innode)
            if cur in outdegree:
                for outnode in outdegree[cur]:
                    if outnode not in visited:
                        visited.add(outnode)
                        queue.append(outnode)
                        self.reorder_cnt += 1




s = Solution()
n = 5
connections = [[1,0],[1,2],[3,2],[3,4]]
# res = 2

n = 3
connections = [[1,0],[2,0]]
# res = 0

n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# res=3

res = s.minReorder(n, connections)
print(res)