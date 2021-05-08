# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def helper(self, root, k, mem):
        if root == None: return
        if k - root.val in mem: return True
        mem.add(root.val)
        return self.helper(root.left, k, mem) or self.helper(root.right, k, mem)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        mem = set()
        return self.helper(root, k, mem)

