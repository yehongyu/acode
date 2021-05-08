"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def helper(self, root, A, B):
        if root == None:
            return None
        if root == A or root == B:
            return root
        left = self.helper(root.left, A, B)
        right = self.helper(root.right, A, B)

        if left == None and right == None:
            return None
        if left != None and right != None:
            return root
        if left != None:
            return left
        if right != None:
            return right


    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        return self.helper(root, A, B)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left.right = TreeNode(5)

s = Solution()
print(s.lowestCommonAncestor(root, root.right.left.right, root.right.left).val)




