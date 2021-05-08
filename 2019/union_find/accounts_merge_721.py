#coding=utf-8

class Solution(object):
    def find(self, root, i):
        while root[i] != -1:
            i = root[i]
        return i

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        n = len(accounts)
        vec = [-1] * n
        if n <= 1:
            return accounts
        name_map = {}
        for i in range(n):
            account = accounts[i]
            name = account[0]
            if name not in name_map:
                name_map[name] = []
            name_map[name].append(i)
        root = [-1] * n
        res = []
        for name in name_map.keys():
            a_list = name_map[name]
            if a_list >= 2:
                inters = []
                for i in a_list:
                    for j in a_list:
                        if i < j:
                            if len(set.intersection(set(accounts[i][1:]), set(accounts[j][1:]))) > 0:
                                inters.append([i, j])
                parts = {}
                for s, e in inters:
                    x = self.find(root, s)
                    y = self.find(root, e)
                    if x != y:
                        root[x] = y
                for i in a_list:
                    x = self.find(root, i)
                    if x not in parts:
                        parts[x] = []
                    parts[x].append(i)
                for key in parts.keys():
                    a_list = parts[key]
                    a_set = set()
                    for i in a_list:
                        a_set.update(accounts[i][1:])
                    res.append([name] + sorted(list(a_set)))
            else:
                a_set = set()
                for i in a_list:
                    a_set.update(accounts[i][1:])
                res.append([name] + sorted(list(a_set)))
        return res




s = Solution()
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["Mary", "mary@mail.com"]]
accounts = [["David","David0@m.co","David1@m.co"],
            ["David","David3@m.co","David4@m.co"],
            ["David","David4@m.co","David5@m.co"],
            ["David","David2@m.co","David3@m.co"],
            ["David","David1@m.co","David2@m.co"]]
res = s.accountsMerge(accounts)
for item in res:
    print(item)







