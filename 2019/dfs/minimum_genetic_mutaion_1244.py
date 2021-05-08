class Solution:
    """
    @param start:
    @param end:
    @param bank:
    @return: the minimum number of mutations needed to mutate from "start" to "end"
    """

    def get_next(self, bank, cur):
        res = []
        for mutation in bank:
            cnt = 0
            for i in range(len(cur)):
                if mutation[i] != cur[i]:
                    cnt += 1
            if cnt == 1:
                res.append(mutation)
        return res

    def minMutation(self, start, end, bank):
        # Write your code here
        n = len(start)
        if n <= 0: return -1
        if len(start) != len(end): return -1
        if start == end: return 0
        queue = [[start, 0]]
        while len(queue) > 0:
            cur, cnt = queue[0]; queue.pop(0)
            nexts = self.get_next(bank, cur)
            for next in nexts:
                if next == end: return cnt+1
                queue.append([next, cnt+1])
        return -1

s = Solution()
start = 'AACCGGTT'
end = 'AACCGGTA'
bank = ["AACCGGTA"]
print(s.minMutation(start, end, bank))