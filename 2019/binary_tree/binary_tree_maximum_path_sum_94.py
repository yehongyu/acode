"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

import sys
minint = -sys.maxsize - 1

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def helper(self, root):
        if root == None:
            return minint, minint
        l_maxsum, l_rootsum = self.helper(root.left)
        r_maxsum, r_rootsum = self.helper(root.right)
        l_maxrootsum = max(l_rootsum, 0)
        r_maxrootsum = max(r_rootsum, 0)
        rootsum = max(l_maxrootsum + root.val, r_maxrootsum + root.val)
        maxsum = max(l_maxsum, r_maxsum, l_maxrootsum + root.val + r_maxrootsum)
        return maxsum, rootsum

    def maxPathSum(self, root):
        # write your code here
        return self.helper(root)[0]

    def maxPathSumFromRoot(self, root):
        if root == None:
            return minint
        left = self.maxPathSumFromRoot(root.left)
        right = self.maxPathSumFromRoot(root.right)
        maxleft = max(left, 0)
        maxright = max(right, 0)
        res = max(root.val + maxleft, root.val + maxright)
        print(root.val, left, right, res)
        return res

    def maxPathSumFromRootToLeaf(self, root):
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root.val
        left = self.maxPathSumFromRootToLeaf(root.left)
        right = self.maxPathSumFromRootToLeaf(root.right)
        if left == None:
            return root.val + right
        if right == None:
            return root.val + left
        res = max(root.val + left, root.val + right)
        print(root.val, left, right, res)
        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(-5)
root.right.left.right = TreeNode(5)

s = Solution()
#print(s.maxPathSum(root))
#print('res', s.maxPathSumFromRoot(root))
print('res', s.maxPathSumFromRootToLeaf(root))



