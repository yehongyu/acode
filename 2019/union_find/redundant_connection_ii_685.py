#coding=utf-8

class Solution(object):
    def findRedundantDirectedConnection_wrong(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        in_degree = {}
        out_degree = {}
        for s, e in edges:
            if s not in out_degree:
                out_degree[s] = []
            out_degree[s].append(e)
            if e not in in_degree:
                in_degree[e] = []
            in_degree[e].append(s)
        print('in', in_degree)
        print('out', out_degree)
        queue = []
        for node in range(1, n+1):
            if node not in out_degree:
                queue.append(node)
            elif node not in in_degree:
                queue.append(node)
        while len(queue) > 0:
            print('queue', queue)
            node = queue[0]
            queue = queue[1:]
            if node in in_degree and len(in_degree[node]) >= 2:
                for i in range(n-1, -1, -1):
                    if edges[i][1] == node and edges[i][0] in in_degree[node]:
                        print('queue', queue, edges[i])
                        return edges[i]
            elif node in in_degree:
                s = in_degree[node][0]
                print('in pop', node, in_degree)
                in_degree.pop(node)
                print('in pop', node, in_degree)
                print('oout remove', s, node, out_degree)
                out_degree[s].remove(node)
                print('oout remove', s, node, out_degree)
                if len(out_degree[s]) == 0:
                    queue.append(s)
                    out_degree.pop(s)
            elif node in out_degree:
                for e in out_degree[node]:
                    if e in in_degree and len(in_degree[e]) >= 2:
                        for i in range(n-1, -1, -1):
                            if edges[i][1] == e and edges[i][0] in in_degree[e] and edges[i][0]!=node:
                                print('111queue', queue, edges[i])
                                return edges[i]
                    print('in rm', e, node, in_degree)
                    in_degree[e].remove(node)
                    print('in rm', e, node, in_degree)
                    if len(in_degree[e]) == 0:
                        queue.append(e)
                        in_degree.pop(e)
                out_degree.pop(node)
        for i in range(n-1, -1, -1):
            if edges[i][0] in out_degree and edges[i][1] in in_degree:
                return edges[i]

    def find(self, vec, i):
        #print('find', i)
        while vec[i] != -1:
            #print('while find', i, vec[i])
            i = vec[i]
        return i

    def find_path(self, vec, i):
        res = []
        res.append(i)
        while vec[i] != -1:
            res.append(vec[i])
            i = vec[i]
        return res

    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        vec = [0] * (n+1)
        first = None; second = None
        for s, e in edges:
            if vec[e] == 0:
                vec[e] = s
            else:
                first = [vec[e], e]
                second = [s, e]
                vec[e] = 0
        #print(first, second)
        for i in range(n+1): vec[i] = -1
        for s, e in edges:
            x = self.find(vec, s)
            y = self.find(vec, e)
            #print(s, e, x, y)
            if x == y:
                if first:
                    nodes = set()
                    nodes.update(self.find_path(vec, s))
                    nodes.update(self.find_path(vec, e))
                    if second[0] not in nodes:
                        #print('11 first', first)
                        return first
                    else:
                        #print('11 second', second)
                        return second
                else:
                    #print('222', [s, e])
                    return [s, e]
            vec[s] = e
        return second


s = Solution()
edges = [[1,2], [1,3], [2,3]] ## [2, 3]
print(s.findRedundantDirectedConnection(edges))
edges = [[1,2], [2,3], [3,4], [4,1], [1,5]] ## [4, 1]
print(s.findRedundantDirectedConnection(edges))
edges = [[1,4],[5,2],[1,3],[4,5],[1,5]]  ## [1, 5]
print(s.findRedundantDirectedConnection(edges))
edges = [[2,1],[3,1],[4,2],[1,4]] ## [2, 1]
print(s.findRedundantDirectedConnection(edges))
edges = [[6,3],[8,4],[9,6],[3,2],[5,10],[10,7],[2,1],[7,6],[4,5],[1,8]] ## [7, 6]
print(s.findRedundantDirectedConnection(edges))
