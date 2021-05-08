# coding=utf-8

class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def is_pald(self, s):
        n = len(s)
        palds = []
        for i in range(n):
            palds.append([False] * n)
        for i in range(n):
            palds[i][i] = True
        for step in range(1, n):
            for i in range(0, n-step):
                j = i + step
                if step <= 2:
                    palds[i][j] = s[i] == s[j]
                else:
                    palds[i][j] = (s[i] == s[j]) and palds[i+1][j-1]
        return palds


    def helper(self, res, path, s, palds, start):
        n = len(palds)
        if start >= n:
            res.append(path[0:])
        for i in range(start, n):
            if not palds[start][i]:
                continue
            path.append(s[start:i+1])
            self.helper(res, path, s, palds, i+1)
            path.pop(len(path)-1)

    def partition(self, s):
        # write your code here
        n = len(s)
        palds = self.is_pald(s)
        res = []
        path = []
        self.helper(res, path, s, palds, 0)
        return res


s = Solution()
res = s.is_pald("aabad")
for item in res:
    print(item)
print(s.partition("aabad"))
print(s.partition("aab"))
