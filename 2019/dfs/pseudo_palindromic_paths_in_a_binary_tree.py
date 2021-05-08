# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pseudoPalindromicPaths(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        status = [0] * 10
        self.palin_cnt = 0
        self.dfs(status, root)
        return self.palin_cnt

    def dfs(self, status, root):
        print("start", root.val, status)
        if root == None: return
        status[root.val] += 1
        if not root.left and not root.right:
            odd = 0
            for val in status: odd += val % 2
            if odd in [0, 1]: self.palin_cnt += 1
            print("leaf", root.val, status, odd, self.palin_cnt)
        if root.left:
            self.dfs(status, root.left)
        if root.right:
            self.dfs(status, root.right)
        status[root.val] -= 1
        print("end", root.val, status)


s = Solution()
root = TreeNode(2)
root.left = TreeNode(3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right = TreeNode(1)
root.right.right = TreeNode(1)
# 2

root = TreeNode(2)
root.left = TreeNode(1)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(1)
root.left.right.right = TreeNode(1)
# 1

root = TreeNode(9)
# 1
res = s.pseudoPalindromicPaths(root)
print(res)
