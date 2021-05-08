# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def helper(self, root, val):
        if root == None: return -1
        if root.val != val:
            return root.val
        left = self.helper(root.left, val)
        right = self.helper(root.right, val)
        if left != -1 and right != -1:
            return min(left, right)
        elif left == -1:
            return right
        elif right == -1:
            return left

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return -1
        return self.helper(root, root.val)

    def mergeTrees(self, t1, t2):
        if t1 == None and t2 == None:
            return None
        if t1 == None:
            root = TreeNode(t2.val)
            root.left = self.mergeTrees(None, t2.left)
            root.right = self.mergeTrees(None, t2.right)
        elif t2 == None:
            root = TreeNode(t1.val)
            root.left = self.mergeTrees(None, t1.left)
            root.right = self.mergeTrees(None, t1.right)
        else:
            root = TreeNode(t1.val+t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
        return root

    def allPossibleFBT(self, N):
        res = []
        if N <= 0 or N % 2 == 0: return []
        if N == 1: return [TreeNode(0)]
        for i in range(1, N-1, 2):
            lefts = self.allPossibleFBT(i)
            rights = self.allPossibleFBT(N-1-i)
            for left in lefts:
                for right in rights:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res

    def __init__(self):
        self.max_count = 0
        self.cur_count = 0
        self.cur_val = None

    def inorder(self, root, res):
        if root == None: return
        if root.left:
            self.inorder(root.left, res)
        self.cur_count += 1
        if root.val != self.cur_val:
            self.cur_count = 1
            self.cur_val = root.val
        if self.cur_count > self.max_count:
            self.max_count = self.cur_count
            del res[0:]
            res.append(root.val)
        elif self.cur_count == self.max_count:
            res.append(root.val)
        self.inorder(root.right, res)


    def findMode(self, root):
        res = []
        self.inorder(root, res)
        return res

    def frequent(self, root, res, n_map):
        if root == None: return 0
        left = self.frequent(root.left, res, n_map)
        right = self.frequent(root.right, res, n_map)
        val = root.val + left + right
        if val not in n_map: n_map[val] = 0
        n_map[val] += 1
        if n_map[val] > self.max_count:
            self.max_count = n_map[val]
            res.clear()
            res.append(val)
        elif n_map[val] == self.max_count:
            res.append(val)
        return val

    def findFrequentTreeSum(self, root):
        if root == None: return None
        res = []
        n_map = {}
        self.frequent(root, res, n_map)
        return res


s = Solution()
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-5)
print(s.findFrequentTreeSum(root))


