class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        if n <= 1: return 0
        map = {}; res = 0
        for i in range(n):
            word = words[i]
            map[word] = 0
            for ch in word:
                map[word] |= 1 << (ord(ch)-ord('a'))
            for j in range(i):
                if map[words[j]] & map[word] == 0:
                    res = max(res, len(words[j]) * len(word))
        return res

s = Solution()
words = ["a","aa","aaa","aaaa"]
words = ["a","ab","abc","d","cd","bcd","abcd"]
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print(s.maxProduct(words))
