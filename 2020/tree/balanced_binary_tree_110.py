# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def helper(self, root):
        # return (isBalanced, maxDepth)
        if root == None: return (True, 0)
        left_res, left_depth = self.helper(root.left)
        right_res, right_depth = self.helper(root.right)
        depth = 1 + max(left_depth, right_depth)
        if not left_res or not right_res:
            return (False, depth)
        if abs(left_depth-right_depth) > 1:
            return (False, depth)
        return (True, depth)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        res, depth = self.helper(root)
        return res
