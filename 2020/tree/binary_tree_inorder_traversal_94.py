# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def inorderTraversalWithRecusion(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        left_res = self.inorderTraversalWithRecusion(root.left)
        right_res = self.inorderTraversalWithRecusion(root.right)

        return left_res + [root.val] + right_res


    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        stack = []; p = root
        res = []
        while len(stack) > 0 or p:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop(-1)
            res.append(p.val)
            p = p.right
        return res

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        stack = []; p = root
        res = []
        while len(stack) > 0 or p:
            while p:
                res.append(p.val)
                stack.append(p)
                p = p.left
            p = stack.pop(-1)
            p = p.right
        return res

    def postorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        stack = []; stack.append(root)
        res = []
        while len(stack) > 0:
            node = stack.pop(-1)
            res = [node.val] + res
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        stack = []; p = root
        res = []
        while len(stack) > 0 or p:
            if p:
                stack.append(p)
                res = [p.val] + res
                p = p.right
            else:
                node = stack.pop(-1)
                p = node.left
        return res

    def balance_healper(self, root):
        # return (isBST, left_max_val, right_max_val)
        if root == None: return (True, 0)
        l_valid, l_depth = self.balance_healper(root.left)
        r_valid, r_depth = self.balance_healper(root.right)
        depth = 1 + max(l_depth, r_depth)
        if not l_valid or not r_valid:
            return (False, depth)
        if abs(l_depth-r_depth) > 1:
            return (False, depth)
        return (True, depth)

    def isBalance(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.balance_healper(root)[0]

    def bst_helper(self, root):
        if root == None:return (True, None, None)
        l_bst, l_min, l_max = self.bst_helper(root.left)
        r_bst, r_min, r_max = self.bst_helper(root.right)
        print(root.val, ", left:", l_bst, l_min, l_max)
        print(root.val, ", right:", r_bst, r_min, r_max)
        cur_min = root.val; cur_max = root.val
        if not l_bst or not r_bst:
            return (False, None, None)
        if l_max != None:
            if l_max <= root.val:
                cur_min = l_min
            else:
                return (False, None, None)
        if r_min != None:
            if r_min >= root.val:
                cur_max = r_max
            else:
                return (False, None, None)
        return (True, cur_min, cur_max)

    def bst_helper_top2down(self, root, min_val, max_val):
        if root == None: return True
        if root.val <= min_val or root.val >= max_val: return False
        left = self.bst_helper_top2down(root.left, min_val, root.val)
        if not left: return False
        return self.bst_helper_top2down(root.right, root.val, max_val)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import  sys
        max_val = sys.maxsize
        min_val = -sys.maxsize - 1
        return self.bst_helper_top2down(root, min_val, max_val)

    # 543. Diameter of Binary Tree
    # The diameter of a binary tree is the length of the longest path
    # between any two nodes in a tree.
    # This path may or may not pass through the root.
    def diameter_helper(self, root):
        if root == None: return (0, 0)
        l_root2leaf, l_max_path = self.diameter_helper(root.left)
        r_root2leaf, r_max_path = self.diameter_helper(root.right)
        root2leaf = 1 + max(l_root2leaf, r_root2leaf)
        max_path = 1 + l_root2leaf + r_root2leaf
        max_path = max(max_path, l_max_path, r_max_path)
        return (root2leaf, max_path)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        root2leaf, max_path = self.diameter_helper(root)
        if max_path > 0:
            return max_path - 1
        else:
            return 0

    # 124. Binary Tree Maximum Path Sum
    # a path is defined as any node sequence from some starting node to any node
    def maxPathSum_helper(self, root):
        import sys
        if root == None: return (0, -sys.maxsize-1)
        l_root2leaf, l_max_path_sum = self.maxPathSum_helper(root.left)
        r_root2leaf, r_max_path_sum = self.maxPathSum_helper(root.right)
        root2leaf = max(root.val, root.val + l_root2leaf, root.val + r_root2leaf)
        max_path_sum = max(root2leaf, root.val + l_root2leaf + r_root2leaf,
                           l_max_path_sum, r_max_path_sum)
        return root2leaf, max_path_sum

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return None
        root2leaf, max_path_sum = self.maxPathSum_helper(root)
        return max_path_sum

    # 235. Lowest Common Ancestor of a Binary Search Tree
    def lowestCommonAncestor22(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None or p == None or q == None:
            return None
        if p == q: return p
        if p.val > q.val:
            tmp = p; p = q; q = tmp
        print(root.val, p.val, q.val)
        if p.val <= root.val <= q.val:
            return root
        elif q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

    # 236. Lowest Common Ancestor of a Binary Tree
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None or p == None or q == None:
            return None
        if p == q: return p
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        if left: return left
        return right

    # 105. Construct Binary Tree from Preorder and Inorder Traversal
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) != len(inorder): return None
        if len(preorder) == 0: return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1: return root
        val = preorder[0]
        pos = None
        for i in range(len(inorder)):
            if inorder[i] == val:
                pos = i; break
        root.left = self.buildTree(preorder[1:pos+1], inorder[0:pos])
        root.right = self.buildTree(preorder[pos+1:], inorder[pos+1:])
        return root

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(postorder) != len(inorder): return None
        if len(postorder) == 0: return None
        val = postorder[-1]
        root = TreeNode(val)
        if len(postorder) == 1: return root
        pos = None
        for i in range(len(inorder)):
            if inorder[i] == val:
                pos = i; break
        root.left = self.buildTree(inorder[0:pos], postorder[0:pos])
        root.right = self.buildTree(inorder[pos+1:], postorder[pos:-1])
        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        size = len(nums)
        if size <= 0: return None
        mid = int((size-1) / 2)
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

    def hasPathSum_helper(self, root, sum):
        if root == None: return False
        if root.left == None and root.right == None and sum == root.val: return True
        left_res = self.hasPathSum_helper(root.left, sum-root.val)
        if left_res: return True
        return self.hasPathSum_helper(root.right, sum-root.val)

    # sum of root-to-leaf path is equal to sum
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None: return False
        return self.hasPathSum_helper(root, sum)

    # 687. Longest Univalue Path
    # return the length of the longest path,
    # where each node in the path has the same value.
    # This path may or may not pass through the root.
    def longestUnivaluePath_helper(self, root):
        # return from_root_path, max_path
        import sys
        if root == None: return (0, -sys.maxsize-1)
        l_from_root_path, l_max = self.longestUnivaluePath_helper(root.left)
        r_from_root_path, r_max = self.longestUnivaluePath_helper(root.left)
        from_root_path = 1
        if root.left and root.left.val == root.val:
            from_root_path = max(from_root_path, 1+l_from_root_path)
        if root.right and root.right.val == root.val:
            from_root_path = max(from_root_path, 1+r_from_root_path)
        max_path = max(from_root_path, l_max, r_max)
        if root.left and root.right and root.left.val == root.right.val and root.left.val==root.val:
            max_path = max(max_path, 1+ l_from_root_path+r_from_root_path)
        print(root.val, from_root_path, max_path)
        return from_root_path, max_path

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return -1
        _, max_path = self.longestUnivaluePath_helper(root)
        return max_path-1

    # Find the total sum of all root-to-leaf numbers.
    def sumNumbers_helper(self, root, val):
        if root == None: return 0
        val = val * 10 + root.val
        if root.left == None and root.right==None: return val
        left = self.sumNumbers_helper(root.left, val)
        right = self.sumNumbers_helper(root.right, val)
        return left + right

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumNumbers_helper(root, 0)

    # is s a subtree of t
    def isSametree(self, s, t):
        if s == None and t == None: return True
        if s == None or t==None: return False
        if s.val == t.val:
            same_left = self.isSametree(s.left, t.left)
            same_right = self.isSametree(s.right, t.right)
            return same_left and same_right
        return False


    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None and t == None: return True
        if s == None or t==None: return False
        if self.isSametree(s, t): return True
        elif self.isSubtree(s.left, t): return True
        else: return self.isSubtree(s.right, t)


    # Given the root of a binary tree, return all duplicate subtrees.
    # For each kind of duplicate subtrees, you only need to return the root node of any one of them.
    def findDuplicateSubtrees_helper(self, root, mem, res):
        if root == None: return "#"
        left_str = self.findDuplicateSubtrees_helper(root.left, mem, res)
        right_str = self.findDuplicateSubtrees_helper(root.right, mem, res)
        cur_str = ','.join([str(root.val), left_str, right_str])
        print('left:', left_str)
        print('right:', right_str)
        if cur_str not in mem:
            mem[cur_str] = 0
        elif mem[cur_str] == 1:
            res.append(root)
        mem[cur_str] += 1
        print(cur_str, mem, len(res))
        return cur_str


    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        mem = {}
        res = []
        self.findDuplicateSubtrees_helper(root, mem, res)
        return res

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        queue = [(root, 1)]
        max_width = 0
        while len(queue) > 0:
            size = len(queue)
            left = None; right = None
            for i in range(size):
                node, idx = queue.pop(0)
                if i == 0: left = idx
                if i == size-1: right = idx
                if node.left:
                    queue.append((node.left, 2*idx))
                if node.right:
                    queue.append((node.right, 2*idx+1))
            max_width = max(max_width, right-left+1)
        return max_width

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) <= 0: return None
        pos = 0; max_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > max_num:
                pos = i; max_num = nums[i]
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[0:pos])
        root.right = self.constructMaximumBinaryTree(nums[pos+1:])
        return root

    # Find the lexicographically smallest string that
    # starts at a leaf of this tree and ends at the root.
    def smallestFromLeaf_helper(self, root, suffix, res):
        if root == None: return
        suffix = chr(ord('a') + root.val) + suffix
        if not root.left and not root.right:
            if len(res) == 0: res.append(suffix)
            else: res[0] = min(res[0], suffix)
            return
        if root.left:
            self.smallestFromLeaf_helper(root.left, suffix, res)
        if root.right:
            self.smallestFromLeaf_helper(root.right, suffix, res)

    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root == None: return ""
        res = []
        self.smallestFromLeaf_helper(root, "", res)
        return res[0]


    def subtreeWithAllDeepest_helper(self, root):
        if root == None: return (None, 0)
        l_subtree, l_depth = self.subtreeWithAllDeepest_helper(root.left)
        r_subtree, r_depth = self.subtreeWithAllDeepest_helper(root.right)
        depth = 1 + max(l_depth, r_depth)
        if l_depth == r_depth:
            return (root, depth)
        elif l_depth > r_depth:
            return (l_subtree, depth)
        elif l_depth < r_depth:
            return (r_subtree, depth)

    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None: return None
        subtree, depth = self.subtreeWithAllDeepest_helper(root)
        return subtree

    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        queue = [(root, 0)]
        while len(queue) > 0:
            size = len(queue)
            pre = None
            for i in range(size):
                node, level = queue.pop(0)
                if node.left: queue.append((node.left, level+1))
                if node.right: queue.append((node.right, level+1))
                if level % 2 == 0 and node.val % 2 == 0:
                    return False
                if level % 2 == 1 and node.val % 2 == 1:
                    return False
                print(level, node.val, pre)
                if i == 0:
                    pre = node.val
                    continue
                if level % 2 == 0 and node.val <= pre:
                    return False
                if level % 2 == 1 and node.val >= pre:
                    return False
                pre = node.val
        return True

    # 230. Kth Smallest Element in a BST
    # Given a binary search tree, write a function kthSmallest
    # to find the kth smallest element in it.
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(12)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    #root.left.left.left = TreeNode(12)
    #root.left.left.right = TreeNode(8)

    root.right = TreeNode(1)
    #root.right.left = TreeNode(7)
    #root.right.left.left = TreeNode(6)
    #root.right.right = TreeNode(9)
    #root.right.right.right = TreeNode(2)

    s = Solution()
    #res = s.inorderTraversal(root)
    #res = s.preorderTraversal(root)
    #res = s.postorderTraversal(root)
    #res = s.isValidBST(root)
    #res = s.diameterOfBinaryTree(root)
    #res = s.maxPathSum(root)
    #res = s.lowestCommonAncestor(root, root.left, root.left.right)
    #res = s.sortedArrayToBST([1,2,3,4,5,6])
    #res = s.hasPathSum(root, 1)
    #res = s.longestUnivaluePath(root)
    #res = s.sumNumbers(root)
    #res = s.isSubtree(root, None)
    #res = s.findDuplicateSubtrees(root)
    #res = s.widthOfBinaryTree(root)
    #res = s.smallestFromLeaf(root)
    #res = s.subtreeWithAllDeepest(root)
    res = s.isEvenOddTree(root)
    print('is valid bst:', res)

