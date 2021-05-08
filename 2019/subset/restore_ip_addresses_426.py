#coding=utf-8

class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """

    def helper(self, res, path, s, start):
        n = len(s)
        if len(path) == 4 and start == n:
            res.append(path[0:])
        if len(path) >= 4:
            return
        if start >= n:
            return
        for i in range(start, max(start+3, n)):
            if int(s[start:i+1]) > 255:
                continue
            if s[start] == '0' and i>start:
                continue
            path.append(s[start:i+1])
            self.helper(res, path, s, i+1)
            path.pop(len(path)-1)

    def restoreIpAddresses(self, s):
        # write your code here
        n = len(s)
        if n < 4:
            return []
        res = []
        path = []
        self.helper(res, path, s, 0)
        ip_res = []
        for item in res:
            ip_res.append('.'.join(item))
        return ip_res

s = Solution()
print(s.restoreIpAddresses("25525511135"))
print(s.restoreIpAddresses("1116512311"))
print(s.restoreIpAddresses("010010"))
print(s.restoreIpAddresses("00000"))
