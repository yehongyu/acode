"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        res = []
        if root == None:
            return res
        stack = []
        cur = root
        while cur != None:
            stack.append(cur)
            cur = cur.left
        while len(stack) > 0:
            node = stack[-1]
            stack.pop(-1)
            if k1 <= node.val <= k2:
                res.append(node.val)
            cur = node.right
            while cur != None:
                stack.append(cur)
                cur = cur.left
        return res

root = TreeNode(1)
root.left = TreeNode(-3)
root.right = TreeNode(8)
root.right.left = TreeNode(4)
root.right.left.right = TreeNode(5)

s = Solution()
print(s.searchRange(root, 1, 10))
