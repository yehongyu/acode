# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree_pre_in(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) != len(inorder):
            return None
        n = len(preorder)
        if n == 0: return None
        val = preorder[0]
        root = TreeNode(val)
        if n == 1: return root
        for i in range(n):
            if val == inorder[i]:
                break
        if i >= n: return None
        root.left = self.buildTree(preorder[1:i+1], inorder[0:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) != len(inorder):
            return None
        n = len(inorder)
        if n == 0: return None
        val = postorder[-1]
        root = TreeNode(val)
        if n == 1: return root
        for i in range(n):
            if val == inorder[i]:
                break
        if i >= n: return None
        root.left = self.buildTree(inorder[0:i], postorder[0:i])
        root.right = self.buildTree(inorder[i+1:n], postorder[i:n-1])
        return root

    def tree2str(self, t):
        if t == None: return ''
        left = ''; right = ''
        if t.right:
            right = '(' + self.tree2str(t.right) + ')'
            left = '()'
        if t.left:
            left = '(' + self.tree2str(t.left) + ')'
        return str(t.val) + left + right


def show_tree(root):
    if root == None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        size = len(queue)
        level_res = []
        for i in range(size):
            node = queue[0]
            queue.pop(0)
            level_res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        print(level_res)


s = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
#show_tree(s.buildTree(preorder, inorder))
#show_tree(s.buildTree(inorder, postorder))
tree = s.buildTree(inorder, postorder)
print(s.tree2str(tree))



