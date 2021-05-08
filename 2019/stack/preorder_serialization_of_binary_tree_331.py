class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')
        if len(preorder) == 1 and preorder[0] == '#':
            return True
        stack = []
        for val in preorder:
            if val != '#':
                stack.append(val)
            else:
                if len(stack) > 0:
                    while len(stack) > 0 and stack[-1] == '#':
                        stack.pop(-1)
                        if len(stack) > 0:
                            stack.pop(-1)
                        else: return False
                    stack.append('#')
                else:
                    return False
        if len(stack) == 1 and stack[-1] == '#':
            return True
        else:
            return False

s = Solution()
preorder = "1,#"
preorder = "9,#,#,1"
preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
print(s.isValidSerialization(preorder))
