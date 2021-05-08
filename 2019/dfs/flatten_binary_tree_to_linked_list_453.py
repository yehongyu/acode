"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def helper(self, root):
        if root == None:
            return None, None
        if root.left == None and root.right == None:
            return root, root
        r_s, r_e = self.helper(root.right)
        if root.left:
            l_s, l_e = self.helper(root.left)
            root.right = l_s
            l_e.right = r_s
        root.left = None
        end = r_e if r_e else l_e
        return root, end

    def flatten(self, root):
        # write your code here
        if root == None:
            return
        self.helper(root)

def show(root):
    if root == None:
        return
    queue = [root]
    i = 0
    while len(queue) > 0:
        i += 1
        qlen = len(queue)
        for i in range(qlen):
            node = queue[0]; queue.pop(0)
            print(node.val, end=' ')
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        print('endl')
        if i > 10:return

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
show(root)
print(s.flatten(root))
show(root)
