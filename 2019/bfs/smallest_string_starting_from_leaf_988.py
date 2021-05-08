# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self, root, suffix, res):
        if not root: return
        cur = chr(ord('a')+root.val) + suffix
        if not root.left and not root.right:
            if len(res) <= 0: res.append(cur)
            elif res[0] > cur: res[0] = cur
            return
        if root.left:
            self.dfs(root.left, cur, res)
        if root.right:
            self.dfs(root.right, cur, res)
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root == None: return ''
        res = []
        self.dfs(root, '', res)
        return res[0]

s = Solution()
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
print(s.smallestFromLeaf(root))

