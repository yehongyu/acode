#coding=utf-8

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def helper(self, letter_map, res, path, digits, start):
        if start >= len(digits):
            res.append(path[0:])



    def letterCombinations(self, digits):
        # write your code here
        letter_map = {
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
        if len(digits) == 0:
            return [[]]
        res = []; pre_res = [""]
        for i in range(len(digits)):
            digit = digits[i]
            letters = letter_map[digit]
            for item in pre_res:
                for letter in letters:
                    res.append(item + letter)
            pre_res = res[0:]
            res = []
        return pre_res

s = Solution()
print(s.letterCombinations("23"))
print(s.letterCombinations("5"))
