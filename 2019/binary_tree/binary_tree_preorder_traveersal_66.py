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
    @return: Preorder in ArrayList which contains node values.
    """
    def helper(self, root, res):
        if root == None:
            return
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)

    ## recursion
    def preorderTraversal_with_recursion(self, root):
        # write your code here
        res = []
        self.helper(root, res)
        return res

    ## divide and conquer
    def preorderTraversal_DC(self, root):
        res = []
        if root == None:
            return res
        left_res = self.preorderTraversal_DC(root.left)
        right_res = self.preorderTraversal_DC(root.right)
        res.append(root.val)
        res.extend(left_res)
        res.extend(right_res)
        return res

    ## iteration
    def preorderTraversal(self, root):
        res = []
        if root == None:
            return res
        stack = []
        stack.append(root)
        while len(stack) > 0:
            node = stack[-1]
            stack.pop(len(stack)-1)
            res.append(node.val)
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)
        return res



root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
s = Solution()
print(s.preorderTraversal(root))
