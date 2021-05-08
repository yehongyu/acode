"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        res = []
        if root == None:
            return res
        queue = []
        queue.append(root)
        flag = False
        while len(queue) > 0:
            size = len(queue)
            level_res = []
            flag = not flag
            for i in range(size):
                node = queue[0]
                queue.pop(0)
                if flag:
                    level_res.append(node.val)
                else:
                    level_res.insert(0, node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            res.append(level_res)
            #res.insert(0, level_res)
        return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(-5)
root.right.left.right = TreeNode(5)

s = Solution()
print('res', s.levelOrder(root))




