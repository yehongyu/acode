# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def helper(self, root, visited, res):
        if not root: return '#'
        left = self.helper(root.left)
        right = self.helper(root.right)
        cur = ','.join(str(root.val), left, right)
        if cur in visited and visited[cur]==1:
            res.append(root)
            visited[cur] += 1
        else:
            visited[cur] = 1
        return cur

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        visited = map
        res = []
        self.helper(root, visited, res)
        return res
