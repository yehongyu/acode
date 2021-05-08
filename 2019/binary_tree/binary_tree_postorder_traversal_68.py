#coding=utf-8

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """

    def helper(self, root, res):
        if root == None:
            return
        self.helper(root.left, res)
        self.helper(root.right, res)
        res.append(root.val)

    # 1. recursion
    def postorderTraversal_recursion(self, root):
        # write your code here
        res = []
        self.helper(root, res)
        return res

    # 2. divide and conquer
    def postorderTraversal_DC(self, root):
        res = []
        if root == None:
            return res
        left = self.postorderTraversal_DC(root.left)
        right = self.postorderTraversal_DC(root.right)
        res.extend(left)
        res.extend(right)
        res.append(root.val)
        return res

    # 3. iteration
    def postorderTraversal(self, root):
        res = []
        if root == None:
            return res
        stack = []
        p = root
        while p != None:
            stack.append([p, False])
            p = p.left
        while len(stack) > 0:
            node, flag = stack[-1]
            stack.pop(len(stack)-1)
            if not flag:
                if node.right != None:
                    stack.append([node, True])
                    p = node.right
                    while p != None:
                        stack.append([p, False])
                        p = p.left
                else:
                    res.append(node.val)
            else:
                res.append(node.val)
        return res


root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(5)
s = Solution()
print(s.postorderTraversal(root))
