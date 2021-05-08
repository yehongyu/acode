class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    if s[i] == ')' and stack[-1]=='(':
                        stack.pop(-1)
                    elif s[i] == '}' and stack[-1]=='{':
                        stack.pop(-1)
                    elif s[i] == ']' and stack[-1]=='[':
                        stack.pop(-1)
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0

s = Solution()
print(s.isValidParentheses('([)]'))
print(s.isValidParentheses('()[]{}'))

