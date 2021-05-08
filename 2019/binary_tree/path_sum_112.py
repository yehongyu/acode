# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def helper(self, root, target):
        if root == None:
            return False
        if root.left == None and root.right == None and root.val == target:
            return True
        return self.helper(root.left, target-root.val) | self.helper(root.right, target-root.val)

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.helper(root, sum)

    def sumNumbersHelper(self, root, cur_sum, res):
        if root == None: return cur_sum
        sum = cur_sum * 10 + root.val
        if root.left == None and root.right == None:
            res[0] += sum
        if root.left != None:
            self.sumNumbersHelper(root.left, sum, res)
        if root.right != None:
            self.sumNumbersHelper(root.right, sum, res)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        res = [0]
        self.sumNumbersHelper(root, 0, res)
        return res[-1]


    def pathSumIIHelper(self, root, sum, res, path):
        if root == None:
            return
        path.append(root.val)
        sum = sum - root.val
        if root.left == None and root.right == None and sum == 0:
            res.append(path[0:])
            path.pop(-1)
            return
        if root.left != None:
            self.pathSumIIHelper(root.left, sum, res, path)
        if root.right != None:
            self.pathSumIIHelper(root.right, sum, res, path)
        path.pop(-1)

    def pathSumII(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        self.pathSumIIHelper(root, sum, res, path)
        return res

    def pathSumIIIDFS(self, root, sum):
        if root == None: return 0
        sum = sum - root.val
        res = 1 if sum == 0 else 0
        res += self.pathSumIIIDFS(root.left, sum)
        res += self.pathSumIIIDFS(root.right, sum)
        return res

    def pathSumIII(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None: return 0
        res = self.pathSumIIIDFS(root, sum)
        res += self.pathSumIII(root.left, sum)
        res += self.pathSumIII(root.right, sum)
        return res







s = Solution()
root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(3)
root.left.left = TreeNode(6)
root.left.right = TreeNode(1)
root.right.left = TreeNode(7)
root.left.left.right = TreeNode(14)
#print(s.hasPathSum(root, 13))
#print(s.sumNumbers(root))
#print(s.pathSumII(root, 14))
#print(s.pathSumIIIHelper(root, 14))
print(s.pathSumIII(root, 14))



