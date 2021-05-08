# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root == None: return root
        if root.val == key:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            cur = root.right;
            while cur and cur.left: cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, cur.val)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        return root

s = Solution()


