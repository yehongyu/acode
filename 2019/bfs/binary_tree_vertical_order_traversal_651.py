"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        # write your code here
        res = []
        if root == None:
            return res
        n_map = {}
        queue = [[root, 0]]
        while len(queue) > 0:
            node, ver_level = queue[0]
            queue.pop(0)
            if ver_level not in n_map:
                n_map[ver_level] = []
            n_map[ver_level].append(node.val)
            if node.left: queue.append([node.left, ver_level-1])
            if node.right: queue.append([node.right, ver_level+1])
        print(n_map.keys())
        for key in range(min(n_map.keys()), max(n_map.keys())+1):
            res.append(n_map[key])
        return res

s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(s.verticalOrder(root))
