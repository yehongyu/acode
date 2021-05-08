class Solution(object):
    def helper(self, res, path, left, right):
        if left > right: return
        if left == 0 and right==0:
            res.append(path)
            return
        if left > 0:
            self.helper(res, path+'(', left-1, right)
        if right > 0:
            self.helper(res, path+')', left, right-1)


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return ['']
        res = []
        path = ''
        self.helper(res, path, n, n)
        return res

s = Solution()
print(s.generateParenthesis(3))