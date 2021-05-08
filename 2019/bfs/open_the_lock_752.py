class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        start = '0000'
        if start in deadends: return -1
        queue = [start]
        visited = set()
        deadends = set(deadends)
        visited.add(start)
        level = 0
        while len(queue) > 0:
            qlen = len(queue)
            level += 1
            for i in range(qlen):
                u = queue[0]; queue.pop(0)
                if u == target: return level-1
                for j in range(4):
                    val = int(u[j])
                    new_val = u[0:j]+str((val + 1) % 10)+u[j+1:]
                    if new_val not in deadends and new_val not in visited:
                        visited.add(new_val)
                        queue.append(new_val)
                    new_val = u[0:j]+str((val + 9) % 10)+u[j+1:]
                    if new_val not in deadends and new_val not in visited:
                        visited.add(new_val)
                        queue.append(new_val)
        return -1

s = Solution()
deadends = ["0201","0101","0102","1212","2002"]; target = "0202"
print(s.openLock(deadends, target))
