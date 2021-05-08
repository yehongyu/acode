"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

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


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if root == None:
            return node
        if node.val <= root.val:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)
        return root

root = TreeNode(1)
root.left = TreeNode(-3)
root.right = TreeNode(8)
root.right.left = TreeNode(4)
root.right.left.right = TreeNode(5)

s = Solution()
node = TreeNode(3)
show_tree(root)
s.insertNode(root, node)
show_tree(root)

