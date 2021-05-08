# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def valid(self, root, mn, mx):
        if root == None: return True
        if mn <= root.val <= mx:
            return self.valid(root.left, mn, root.val) and self.valid(root.right, root.val, mx)
        return False

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        import sys
        return self.valid(root, -sys.maxsize-1, sys.maxsize)


