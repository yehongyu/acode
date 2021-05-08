class Solution(object):
    def dfs(self, S, res, cur, pos):
        print(cur, pos)
        if pos == len(S):
            res.append(cur)
            return
        if S[pos].isdigit():
            self.dfs(S, res, cur+S[pos], pos + 1)
        else:
            for ch in [S[pos].lower(), S[pos].upper()]:
                self.dfs(S, res, cur+ch, pos + 1)

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        cur = ''
        self.dfs(S, res, cur, 0)
        return res

s = Solution()
print(s.letterCasePermutation('a1b2'))