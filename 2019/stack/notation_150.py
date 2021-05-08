class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        n = len(tokens)
        if n <= 0: return 0
        d_stack = []
        for token in tokens:
            if token.isdigit() or (token.startswith('-')
                                   and len(token) > 1
                                   and token[1:].isdigit()):
                d_stack.append(int(token))
            else:
                b = d_stack[-1]; d_stack.pop(-1)
                a = d_stack[-1]; d_stack.pop(-1)
                if token == '+':
                    c = a + b
                elif token == '-':
                    c = a - b
                elif token == '*':
                    c = a * b
                elif token == '/':
                    c = int(abs(a) / abs(b))
                    if a * b < 0:
                        c = 0-c
                print(a, token, b, c)
                d_stack.append(c)
            print(token, d_stack)
        return d_stack[-1]

s = Solution()
tokens = ["2", "1", "+", "3", "*"]
tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(s.evalRPN(tokens))
