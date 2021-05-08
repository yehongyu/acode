class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        n = len(A)
        if n == 0: return 0
        if n == 1: return A[0]
        p0 = 0;p1 = 0;p2 = 0
        res = max(p1, p2)
        for i in range(1, n+1):
            cur = max(p0, p1) + A[i-1]
            res = max(res, cur)
            p0 = p1
            p1 = p2
            p2 = cur
        return res

    def houseRobber2(self, nums):
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        return max(self.houseRobber(nums[0:n-1]), self.houseRobber(nums[1:]))

    def helper(self, root, res):
        if root == None:
            return 0, [0, 0], [0, 0, 0, 0]
        l_root, l1, l2 = self.helper(root.left, res)
        r_root, r1, r2 = self.helper(root.right, res)
        l1_l = max(l1[0], l2[0] + l2[1])
        l1_r = max(l1[1], l2[2] + l2[3])
        r1_l = max(r1[0], r2[0] + r2[1])
        r1_r = max(r1[1], r2[2] + r2[3])
        root_sum = root.val + l1_l + l1_r + r1_l + r1_r
        print(root_sum, l_root, r_root)
        res[-1] = max(res[-1], root_sum)
        return root_sum, [l_root, r_root], [l1_l, l1_r, r1_l, r1_r]

    def houseRobber3_DC(self, root):
        if root == None:
            return 0
        res = [0]
        dummy = TreeNode(0)
        dummy.left = root
        root_sum, l1_nodes,l2_nodes = self.helper(dummy, res)
        return res[-1]

    def helper_map(self, root, n_map):
        if root == None: return 0
        if root in n_map: return n_map[root]
        val = 0
        if root.left:
            val += self.helper_map(root.left.left, n_map) + self.helper_map(root.left.right, n_map)
        if root.right:
            val += self.helper_map(root.right.left, n_map) + self.helper_map(root.right.right, n_map)
        res = max(val + root.val, self.helper_map(root.left, n_map) + self.helper_map(root.right, n_map))
        n_map[root] = res
        return res


    def houseRobber3(self, root):
        if root == None:
            return 0
        n_map = {}
        return self.helper_map(root, n_map)

s = Solution()
'''
print(s.houseRobber([3, 8, 4]))
print(s.houseRobber([5, 2, 1, 3]))

print(s.houseRobber2([3, 6, 4]))
print(s.houseRobber2([2, 3, 2, 3]))
'''

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left= TreeNode(5)
root.left.right = TreeNode(4)
#root.right.right = TreeNode(1)
print(s.houseRobber3(root))