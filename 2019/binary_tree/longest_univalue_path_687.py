# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def helper(self, root):
        if root == None:
            return 0, 0
        print('beg-val:', root.val)
        if root.left == None and root.right == None:
            return 0, 0
        l_max, l_root_max = self.helper(root.left)
        print('left:', l_max, l_root_max)
        r_max, r_root_max = self.helper(root.right)
        print('right:', r_max, r_root_max)
        root_max = 0
        if root.left != None and root.val == root.left.val:
            root_max = l_root_max + 1
        if root.right != None and root.val == root.right.val:
            root_max = max(root_max, r_root_max + 1)
        cur_max = max(root_max, l_max, r_max)
        if root.left != None and root.right != None and root.val == root.left.val and root.val == root.right.val:
            cur_max = max(cur_max, l_root_max + 2 + r_root_max)
        print('end-val:', root.val, cur_max, root_max)
        return cur_max, root_max


    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.helper(root)
        return res[0]

s = Solution()
root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)

print(s.longestUnivaluePath(root))

