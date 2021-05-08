"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

import sys
maxint = sys.maxsize
minint = - maxint - 1

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def helper(self, root):
        if root == None:
            return True, minint, maxint
        l_is_valid, l_maxkey, l_minkey = self.helper(root.left)
        r_is_valid, r_maxkey, r_minkey = self.helper(root.right)
        is_valid = l_is_valid and r_is_valid and l_maxkey < root.val and r_minkey > root.val
        print('left:', l_is_valid, l_maxkey, l_minkey)
        print('right:', r_is_valid, r_maxkey, r_minkey)
        maxkey = max(r_maxkey, root.val)
        minkey = min(l_minkey, root.val)

        print(is_valid, maxkey, minkey)
        return is_valid, maxkey, minkey

    def isValidBST(self, root):
        # write your code here
        return self.helper(root)[0]

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(2)

#root.right.left = TreeNode(2)
#root.right.left.right = TreeNode(7)

s = Solution()
print(s.isValidBST(root))



