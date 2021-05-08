class Solution:
    """
    @param deadends: the list of deadends
    @param target: the value of the wheels that will unlock the lock
    @return: the minimum total number of turns
    """
    def openLock(self, deadends, target):
        # Write your code here
        start = '0000'
        queue = []
        if start in deadends: return -1
        queue.append([start, 0])
        visited = set(); visited.add(start)
        while len(queue) > 0:
            node, dist = queue[0]; queue.pop(0)
            if node == target: return dist
            for i in range(4):
                for j in [-1, 1]:
                    idx = str((int(node[i]) + j) % 10)
                    nn = node[0:i] + idx + node[i+1:]
                    if nn not in visited and nn not in deadends:
                        visited.add(nn)
                        queue.append([nn, dist+1])
        return -1

s = Solution()
deadends = ["8888"]
target = '0009'
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(s.openLock(deadends, target))



