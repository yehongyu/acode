# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def dfs(self, root, voyage, res):
        if root == None: return True
        if root.val != voyage[0]: return False
        voyage.pop(0)
        if root.left and root.left.val == voyage[0]:
            l_res = self.dfs(root.left, voyage, res)
            if not l_res: return False
            return self.dfs(root.right, voyage, res)
        if root.right and root.right.val == voyage[0]:
            if root.left: res.append(root.val)
            r_res = self.dfs(root.right, voyage, res)
            if not r_res: return False
            return self.dfs(root.left, voyage, res)
        return not root.left and not root.right

    def flipMatchVoyage_pop(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        if root == None and len(voyage)==0: return []
        res = []
        state = self.dfs(root, voyage, res)
        if state and len(voyage)==0:
            return res
        return [-1]

    def dfs2(self, root, voyage, res):
        if root == None: return True
        if root.val != voyage[self.idx]: return False
        self.idx += 1
        if root.left and root.left.val == voyage[self.idx]:
            return self.dfs2(root.left, voyage, res) & self.dfs2(root.right, voyage, res)
        if root.right and root.right.val == voyage[self.idx]:
            if root.left: res.append(root.val)
            return self.dfs2(root.right, voyage, res) & self.dfs2(root.left, voyage, res)
        return not root.left and not root.right

    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        if root == None and len(voyage)==0: return []
        res = []
        self.idx = 0
        state = self.dfs2(root, voyage, res)
        if state and len(voyage)== self.idx:
            return res
        return [-1]



s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
voyage = [1,2]
voyage = [1,3,2]
voyage = [1,2,3]
print(s.flipMatchVoyage(root, voyage))