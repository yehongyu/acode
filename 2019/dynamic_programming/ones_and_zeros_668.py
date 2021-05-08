class Solution:
    """
    @param strs: an array with strings include only 0 and 1
    @param m: An integer
    @param n: An integer
    @return: find the maximum number of strings
    """
    def get_one_zero_num(self, s):
        n = len(s)
        if n == 0: return 0, 0
        one = 0
        zero = 0
        for i in range(n):
            if s[i] == '1': one += 1
            else: zero += 1
        return zero, one

    def dfs(self, res, data, path, m, n, pos):
        print('path', pos, m, n, path)
        res[0] = max(res[0], len(path))
        if pos >= len(data):
            return
        for i in range(pos, len(data)):
            cur_zero = m - data[i][0]
            cur_one = n - data[i][1]
            if cur_one >= 0 and cur_zero >= 0:
                path.append(data[i])
                self.dfs(res, data, path, cur_zero, cur_one, i+1)
                path.pop(-1)

    def findMaxForm_dfs(self, strs, m, n):
        # write your code here
        k = len(strs)
        if k <= 0: return 0
        res = [0]
        path = []
        data = []
        for i in range(k):
            zero, one = self.get_one_zero_num(strs[i])
            data.append([zero, one])
        self.dfs(res, data, path, m, n, 0)
        return res[0]

    def findMaxForm(self, strs, m, n):
        # write your code here
        k = len(strs)
        if k <= 0: return 0
        data = []
        for i in range(k):
            zero, one = self.get_one_zero_num(strs[i])
            data.append([zero, one])
        dp = []
        for i in range(m+1):
            dp.append([0] * (n+1))
        print(dp)
        print(data)
        for t in range(k):
            zero = data[t][0]
            one = data[t][1]
            for i in range(m, zero-1, -1):
                for j in range(n, one-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zero][j-one] + 1)
        print(dp)
        return dp[m][n]


s = Solution()
strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(s.findMaxForm(strs, m, n))