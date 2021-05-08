# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        l_depth = 0
        r_depth = 0
        left = root
        while left:
            left = left.left
            l_depth += 1
        right = root
        while right:
            right = right.right
            r_depth += 1
        if l_depth == r_depth:
            return pow(2, l_depth) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def kthSmallest(self, root, k):
        if root == None or k <= 0: return None
        stack = []
        cur = root
        while cur:
            stack.append(cur)
            cur = cur.left
        while len(stack) > 0:
            node = stack[-1]; stack.pop(-1)
            k -= 1
            if k == 0: return node.val
            cur = node.right
            while cur:
                stack.append(cur)
                cur = cur.left
        return None
