"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: a TreeNode
    @return: a list of integer
    """
    def left_bound(self, root, res):
        if not root or (not root.left and not root.right):
            return
        res.append(root.val)
        if not root.left: self.left_bound(root.right, res)
        self.left_bound(root.left, res)

    def right_bound(self, root, res):
        if not root or (not root.left and not root.right):
            return
        if not root.right: self.right_bound(root.left, res)
        self.right_bound(root.right, res)
        res.append(root.val)

    def leaf(self, root, res):
        if not root:
            return
        if not root.left and not root.right:
            res.append(root.val)
        self.leaf(root.left, res)
        self.leaf(root.right, res)

    def boundaryOfBinaryTree(self, root):
        # write your code here
        res = []
        if root == None:
            return res
        if root.left or root.right:
            res = [root.val]
        self.left_bound(root.left, res)
        print(res)
        self.leaf(root, res)
        print(res)
        self.right_bound(root.right, res)
        print(res)
        return res

s = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
print(s.boundaryOfBinaryTree(root))
