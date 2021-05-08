#coding=utf-8
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        n = len(s)
        words = []
        word = ''
        for i in range(n):
            if s[i] == ' ':
                if len(word) > 0:
                    words.append(word[0:])
                    word = ''
            else:
                word += s[i]
        m = len(words)
        for i in range(m/2):
            tmp = words[i]
            words[i] = words[m-1-i]
            words[m-1-i] = tmp
        return ' '.join(words)

s = Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("  hello  world!  "))


