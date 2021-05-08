class Solution:
    """
    @param pid: the process id
    @param ppid: the parent process id
    @param kill: a PID you want to kill
    @return: a list of PIDs of processes that will be killed in the end
    """
    def killProcess(self, pid, ppid, kill):
        # Write your code here
        graph = {}
        n = len(pid)
        if n <= 0: return []
        for i in range(n):
            if ppid[i] not in graph:
                graph[ppid[i]] = []
            graph[ppid[i]].append(pid[i])
        res = []
        queue = [kill]
        while len(queue) > 0:
            cur_pid = queue[0]; queue.pop(0)
            res.append(cur_pid)
            if cur_pid in graph:
                for n_pid in graph[cur_pid]:
                    queue.append(n_pid)
        return res

s = Solution()
pid = [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 3
print(s.killProcess(pid, ppid, kill))
