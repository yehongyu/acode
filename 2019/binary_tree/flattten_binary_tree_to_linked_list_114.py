# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten_helper(self, root):
        if root == None: return None, None
        print('begin:', root.val)
        left, l_end = self.flatten_helper(root.left)
        right, r_end = self.flatten_helper(root.right)
        root.left = None
        root.right = left
        end = root
        if l_end:
            l_end.right = right
            end = l_end
        else:
            root.right = right
        if r_end:
            end = r_end
        print('end:', root.val, end.val)
        return root, end

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root == None: return None
        return self.flatten_helper(root)[0]




s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
res = s.flatten(root)
while res:
    print(res.val, ',')
    res = res.right
print('end')
