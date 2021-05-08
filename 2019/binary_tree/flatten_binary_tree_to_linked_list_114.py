# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten_recursion(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root == None: return None
        self.flatten(root.left)
        self.flatten(root.right)
        tmp = root.right
        cur = root.left
        root.right = cur
        root.left = None
        while cur.right:
            cur = cur.right
        cur.right = tmp


    def flatten_iteration(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root == None: return
        cur = root
        while cur:
            if cur.left:
                p = cur.left
                while p.right: p = p.right
                p.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root == None: return
        stack = [root]
        while len(stack) > 0:
            cur = stack[-1]; stack.pop(-1)
            if cur.left:
                p = cur.left
                while p.right: p = p.right
                p.right = cur.right
                cur.right = cur.left
                cur.left = None
            if cur.right:
                stack.append(cur.right)
