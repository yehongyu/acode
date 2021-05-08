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
    @return: Inorder in ArrayList which contains node values.
    """

    def helper(self, root, res):
        if root == None:
            return
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)

    # 1. recursion
    def inorderTraversal_recursion(self, root):
        # write your code here
        res = []
        self.helper(root, res)
        return res

    # 2. divide and conquer
    def inorderTraversal_DC(self, root):
        res = []
        if root == None:
            return res
        left_res = self.inorderTraversal_DC(root.left)
        right_res = self.inorderTraversal_DC(root.right)
        res.extend(left_res)
        res.append(root.val)
        res.extend(right_res)
        return res

    # 3.iteration
    def inorderTraversal(self, root):
        res = []
        if root == None:
            return res
        stack = []
        p = root
        while p != None:
            stack.append(p)
            p = p.left
        while len(stack) > 0:
            node = stack[-1]
            stack.pop(len(stack)-1)
            res.append(node.val)
            p = node.right
            while p != None:
                stack.append(p)
                p = p.left
        return res

root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(5)
s = Solution()
print(s.inorderTraversal(root))
