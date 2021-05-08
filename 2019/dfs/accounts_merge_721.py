class Solution(object):

    def dfs(self, graph, visited, email, group):
        group.append(email)
        if email not in graph: return
        for cur in graph[email]:
            if cur in visited: continue
            visited.add(cur)
            self.dfs(graph, visited, cur, group)

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        name_map = {}
        graph = {}
        for account in accounts:
            name = account[0]
            cnt = len(account)
            for i in range(1, cnt):
                name_map[account[i]] = name
                if account[i] not in graph:
                    graph[account[i]] = set()
                graph[account[i]].update(set(account[1:i]+account[i+1:cnt]))
        visited = set()
        res = []
        for email in name_map.keys():
            if email not in visited:
                group = []
                visited.add(email)
                self.dfs(graph, visited, email, group)
                res.append([name_map[email]] + sorted(group))
        return res

s = Solution()
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
print(s.accountsMerge(accounts))



