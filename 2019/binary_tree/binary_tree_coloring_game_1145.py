# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def dfs(self, root, x):
        if root == None: return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        num = l + r + 1
        if root.val == x:
            self.left = l
            self.right = r
        return num

    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        if root == None: return False
        self.dfs(root, x)
        val = max(self.left, self.right, n-1-self.left-self.right)
        return val > x-val
