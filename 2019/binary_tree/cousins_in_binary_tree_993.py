# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def find_father(self, root, key):
        if root == None: return None
        res = None
        if root.left:
            if key == root.left.val:
                return root
            res = self.find_father(root.left, key)
        if not res and root.right:
            if key == root.right.val:
                return root
            res = self.find_father(root.right, key)
        return res

    def get_depth(self, root, key, depth):
        if root == None: return None
        if root.val == key: return depth
        res = None
        if root.left:
            res = self.get_depth(root.left, key, depth+1)
        if not res and root.right:
            res = self.get_depth(root.right, key, depth+1)
        return res

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root == None: return False
        if x == root.val or y == root.val: return False
        father1 = self.find_father(root, x)
        father2 = self.find_father(root, y)
        depth1 = self.get_depth(root, x, 0)
        depth2 = self.get_depth(root, y, 0)
        print(depth1, depth2)
        if depth1 == depth2 and father1 != father2:
            return True
        return False
s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
print(s.isCousins(root, 4,5))
