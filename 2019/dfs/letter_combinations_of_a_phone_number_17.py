class Solution(object):

    def dfs(self, dict, digits, res, path, pos):
        if len(path) == len(digits):
            res.append(path[0:])
            return
        digit = digits[pos]
        for ch in dict[digit]:
            tmp = path + ch
            self.dfs(dict, digits, res, tmp, pos + 1)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter_map = {
            '0': [],
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []
        path = ''
        self.dfs(letter_map, digits, res, path, 0)
        return res

s = Solution()
digits = '23'
print(s.letterCombinations(digits))