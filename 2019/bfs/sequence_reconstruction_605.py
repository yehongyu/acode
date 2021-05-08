class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        if len(seqs) == 1:
            if len(org) != len(seqs[0]): return False
            for j in range(len(org)):
                if org[j] != seqs[0][j]: return False
            return True
        graph = {}
        indegree = {}
        for i in range(len(seqs)):
            if len(seqs[i]) == 0: continue
            if seqs[i][0] not in graph:
                graph[seqs[i][0]] = []
            if seqs[i][0] not in indegree:
                indegree[seqs[i][0]] = 0
            for j in range(1, len(seqs[i])):
                if seqs[i][j-1] not in graph:
                    graph[seqs[i][j-1]] = []
                graph[seqs[i][j-1]].append(seqs[i][j])
                if seqs[i][j] not in indegree:
                    indegree[seqs[i][j]] = 0
                indegree[seqs[i][j]] += 1
        queue = []
        for key in indegree.keys():
            if indegree[key] == 0:
                queue.append(key)
        path = []
        while len(queue) > 0:
            qlen = len(queue)
            if qlen > 1: return False
            for i in range(qlen):
                node = queue[0]; queue.pop(0)
                path.append(node)
                if node not in graph: continue
                for dep in graph[node]:
                    indegree[dep] -= 1
                    if indegree[dep] == 0:
                        queue.append(dep)
        if len(path) != len(indegree): return False
        if len(path) != len(org): return False
        for i in range(len(path)):
            if path[i] != org[i]: return False
        return True

s = Solution()
print(s.sequenceReconstruction([1,2,3], [[1,2],[1,3]]))
print(s.sequenceReconstruction([1,2,3], [[1,2]]))
print(s.sequenceReconstruction([1,2,3], [[1,2],[1,3],[2,3]]))
print(s.sequenceReconstruction([4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]]))
print(s.sequenceReconstruction([1,2], [[1,2]]))
print(s.sequenceReconstruction([], [[]]))




