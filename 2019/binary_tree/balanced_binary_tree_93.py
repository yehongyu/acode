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
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def helper(self, root):
        if root == None:
            return True, 0
        l_isba, l_depth = self.helper(root.left)
        r_isba, r_depth = self.helper(root.right)
        isba = l_isba and r_isba and abs(l_depth - r_depth) <= 1
        return isba, max(l_depth, r_depth) + 1

    def isBalanced(self, root):
        # write your code here
        return self.helper(root)[0]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left.right = TreeNode(5)

s = Solution()
print(s.isBalanced(root))
print(s.isBalanced(root.left))
print(s.isBalanced(root.right))
print(s.isBalanced(root.right.left))


