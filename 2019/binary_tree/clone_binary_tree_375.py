"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree
    @return: root of new tree
    """
    def cloneTree_DC(self, root):
        # write your code here
        if root == None:
            return None
        new_root = TreeNode(root.val)
        new_root.left = self.cloneTree(root.left)
        new_root.right = self.cloneTree(root.right)
        return new_root

    def cloneTree(self, root):
        if root == None:
            return None
        queue = []
        new_root = TreeNode(root.val)
        queue.append([root, new_root])
        while len(queue) > 0:
            top, new_top = queue[0]
            queue.pop(0)
            if top.left:
                new_left = TreeNode(top.left.val)
                new_top.left = new_left
                queue.append([top.left, new_left])
            if top.right:
                new_right = TreeNode(top.right.val)
                new_top.right = new_right
                queue.append([top.right, new_right])
        return new_root




s = Solution()



