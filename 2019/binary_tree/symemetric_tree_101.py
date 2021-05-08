# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def validSymmetric(self, root1, root2):
        if root1 == None and root2 == None: return True
        if root1 == None or root2 == None: return False
        if root1.val != root2.val: return False
        return self.validSymmetric(root1.left, root2.right) and self.validSymmetric(root1.right, root2.left)

    def isSymmetric_DFS(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        return self.validSymmetric(root.left, root.right)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        arr = [root.left, root.right]
        while len(arr) > 0:
            left = arr[0]; arr.pop(0)
            right = arr[-1]; arr.pop(-1)
            if left == None and right == None: continue
            if left == None or right == None: return False
            if left.val != right.val: return False
            arr.insert(0, left.left)
            arr.insert(0, left.right)
            arr.append(right.right)
            arr.append(right.left)
        return True


