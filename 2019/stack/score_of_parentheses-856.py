class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        if n <= 1: return 0
        if n == 2: return 1
        stack = []
        for i in range(n):
            ch = S[i]
            if ch == '(':
                stack.append('(')
            elif ch == ')':
                cur = 0
                while len(stack) > 0 and stack[-1] != '(':
                    cur += stack[-1]
                    stack.pop(-1)
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop(-1)
                    cur = cur * 2 if cur > 0 else 1
                    stack.append(cur)
            print(i, ch, stack)
        res = 0
        while len(stack) > 0:
            res += stack[-1]
            stack.pop(-1)
        return res
s = Solution()
print(s.scoreOfParentheses("()"))
print(s.scoreOfParentheses("(())"))
print(s.scoreOfParentheses("()()"))
print(s.scoreOfParentheses("()(())"))
print(s.scoreOfParentheses("(()(()))"))

