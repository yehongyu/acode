# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        self.good_cnt = 1
        self.dfs(root, root.val)
        return self.good_cnt
    def dfs(self, root, val):
        if root == None: return
        if root.left:
            if root.left.val >= val:
                self.good_cnt += 1
            self.dfs(root.left, max(val, root.left.val))
        if root.right:
            if root.right.val >= val:
                self.good_cnt += 1
            self.dfs(root.right, max(val, root.right.val))


s = Solution()
root = TreeNode(3)
#root.left = TreeNode(3)
#root.left.left = TreeNode(4)
#root.left.right = TreeNode(2)
#root.right = TreeNode(4)
#root.right.left = TreeNode(1)
#root.right.right = TreeNode(5)

res = s.goodNodes(root)
print(res)
