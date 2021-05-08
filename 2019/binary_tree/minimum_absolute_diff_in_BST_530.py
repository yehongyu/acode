# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def helper(self, root, res):
        if root == None: return None, None
        l_min = root.val
        if root.left:
            l_min, l_max = self.helper(root.left, res)
            print('left', root.val, l_max)
            res[0] = min(res[0], root.val-l_max)
        r_max = root.val
        if root.right:
            r_min, r_max = self.helper(root.right, res)
            print('right', root.val, r_min)
            res[0] = min(res[0], r_min-root.val)
        print(l_min, r_max, res)
        return l_min, r_max


    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return -1
        if root.left == None and root.right == None: return -1
        import sys
        res = [sys.maxsize]
        self.helper(root, res)
        return res[0]

s = Solution()
root = TreeNode(600)
root.left = TreeNode(424)
root.right = TreeNode(612)
root.left.right = TreeNode(499)
root.right.right = TreeNode(689)
print(s.getMinimumDifference(root))

