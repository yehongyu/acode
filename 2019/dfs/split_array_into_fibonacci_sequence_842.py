class Solution(object):

    def dfs(self, Str, path, res):
        print(Str, path)
        if len(path) >= 3 and path[-3]+path[-2]!=path[-1]: return False
        if len(Str) == 0 and len(path)>=3:
            for val in path: res.append(val)
            return True
        for i in range(len(Str)):
            cur = Str[:i+1]
            print('11', Str, cur)
            if cur[0] == '0' and len(cur)!= 1: continue
            if int(cur) >= pow(2,31): continue
            print('22', Str, cur)
            path.append(int(cur))
            if self.dfs(Str[i+1:], path, res): return True
            path.pop(-1)


    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        if n < 3: return False
        path = []
        res = []
        if self.dfs(S, path, res):
            return res
        return []
s = Solution()
#print(s.splitIntoFibonacci("123456579"))
print(s.splitIntoFibonacci("11235813"))
