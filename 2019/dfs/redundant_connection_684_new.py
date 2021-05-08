class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        map = {}
        for s, e in edges:
            if s not in map: map[s] = set()
            if e not in map: map[e] = set()
            map[s].add(e)
            map[e].add(s)
        queue = []
        visited = set()
        for cur in map.keys():
            if len(map[cur]) == 1:
                queue.append(cur)
                visited.add(cur)
        while len(queue) > 0:
            cur = queue[0]; queue.pop(0)
            for e in map[cur]:
                map[e].remove(cur)
                if len(map[e]) <= 1 and e not in visited:
                    queue.append(e)
                    visited.add(e)
            map.pop(cur)

        for i in range(n-1, -1, -1):
            s, e = edges[i]
            if s in map and e in map:
                return [s, e]

s = Solution()
edges = [[1,2], [1,3], [2,3]]
edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
print(s.findRedundantConnection(edges))

