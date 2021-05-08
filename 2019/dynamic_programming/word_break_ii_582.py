class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak_i(self, s, wordDict):
        # write your code here
        n = len(s)
        if n <= 0: return True
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(0, i):
                if s[j:i] in wordDict:
                    dp[i] |= dp[j]
        return dp[n]

    def helper(self, s, wordDict, res, path, pos):
        n = len(s)
        if pos == n:
            res.append(path[0:])
            return
        for i in range(pos+1, n+1):
            if s[pos:i] in wordDict:
                path.append(s[pos:i])
                self.helper(s, wordDict, res, path, i)
                path.pop(-1)

    def wordBreak(self, s, wordDict):
        n = len(s)
        if n <= 0: return []
        if not self.wordBreak_i(s, wordDict):
            return []
        res = []
        path = []
        self.helper(s, wordDict, res, path, 0)
        result = []
        for path in res:
            result.append(' '.join(path))
        return result

    def wordBreak3(self, s, dict):
        n = len(s)
        if n <= 0 or len(dict) <= 0: return 0
        s = s.lower()
        for i in range(len(dict)):
            dict[i] = dict[i].lower()
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                if s[j:i] in dict:
                    dp[i] += dp[j]
        return dp[n]


s = Solution()
saa = 'CatMat'
dict = ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
saa = "aaaaaaaa"
dict = ["aaaa","Aa","aaa"]
print(s.wordBreak3(saa, dict))
#print(s.wordBreak("lintcode", ['lint', 'co', 'de', 'code']))


