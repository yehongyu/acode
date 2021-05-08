"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root
    @return: the maximum width of the given tree
    """
    def widthOfBinaryTree_fillNone(self, root):
        # Write your code here
        if root == None: return 0
        queue = []
        queue.append(root)
        res = 0
        while len(queue) > 0:
            qlen = len(queue)
            start = None
            end = None
            for i in range(0, qlen):
                node = queue[0]; queue.pop(0)
                if node == None:
                    queue.append(None)
                    queue.append(None)
                else:
                    if start == None: start = i
                    end = i
                    queue.append(node.left)
                    queue.append(node.right)
            if start == None or end == None:
                break
            else:
                res = max(res, end-start+1)
        return res

    def widthOfBinaryTree(self, root):
        if root == None: return 0
        queue = []
        queue.append([root, 0])
        res = 0
        while len(queue) > 0:
            qlen = len(queue)
            left = None; right = None
            for i in range(qlen):
                node, idx = queue[0]; queue.pop(0)
                print('pop:', node.val, idx)
                if left == None: left = idx
                right = idx
                if node.left: queue.append([node.left, 2*idx+1])
                if node.right: queue.append([node.right, 2*idx+2])
            res = max(res, right-left+1)
            print(left, right, qlen, res)
        return res


s = Solution()
root = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(5)
root.left.left.left = TreeNode(6)
root.right = TreeNode(2)
root.right.right = TreeNode(9)
root.right.right.right = TreeNode(7)


print(s.widthOfBinaryTree(root))

