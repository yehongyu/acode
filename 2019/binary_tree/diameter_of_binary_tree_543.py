# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def helper(self, root):
        if root == None: return -1, -1
        if root.left == None and root.right==None: return 0, 0
        l_path, l_max = self.helper(root.left)
        r_path, r_max = self.helper(root.right)
        root_path = max(l_path, r_path) + 1
        max_path = max(root_path, l_path + r_path + 2, l_max, r_max)
        print(root.val, root_path, max_path)
        return root_path, max_path

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return -1
        return self.helper(root)[1]

s = Solution()
root = TreeNode(1)
#root.left = TreeNode(2)
root.right = TreeNode(3)
#root.left.left = TreeNode(4)
#root.left.right = TreeNode(5)
print(s.diameterOfBinaryTree(root))

