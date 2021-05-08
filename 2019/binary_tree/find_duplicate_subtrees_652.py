# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def helper(self, root, visited, res):
        if root == None:
            return '#'
        l_path = self.helper(root.left, visited, res)
        r_path = self.helper(root.right, visited, res)
        path = ','.join([str(root.val), l_path, r_path])
        if path in visited:
            if visited[path] == 1:
                res.append(root)
            visited[path] += 1
        else:
            visited[path] = 1
        return path

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        visited = {}
        res = []
        self.helper(root, visited, res)
        return res

    def serialize(self, root):
        if root == None: return '#'
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return ','.join([str(root.val), left, right])

    def subTree_helper(self, root, target):
        if root == None: cur = '#'
        else:
            left = self.subTree_helper(root.left, target)
            right = self.subTree_helper(root.right, target)
            if left or right: return True
            cur = ','.join([str(root.val), left, right])
        if cur == target:
            return True
        return False

    def isSubtree(self, s, t):
        target = self.serialize(t)
        return self.subTree_helper(s, target)

    def greater(self, root, val):
        if root == None: return val
        if root.left == None and root.right == None:
            root.val += val
            return root.val
        right = self.greater(root.right, val)
        root.val += right
        left = self.greater(root.left, root.val)
        return left

    def convertBST(self, root):
        if root == None: return root
        self.greater(root, 0)
        return root

    def diff_helper(self, root, path, res):
        if root == None: return
        if root.left == None and root.right == None:
            max_v = min_v = path[0]
            for i in range(1, len(path)):
                max_v = max(max_v, path[i])
                min_v = min(min_v, path[i])
            res[0] = max(res[0], max_v-min_v)
        elif root.left:
            path.append(root.left.val)
            self.diff_helper(root, path, res)
            path.pop(-1)
        elif root.right:
            path.append(root.right.val)
            self.diff_helper(root, path, res)
            path.pop(-1)

    def maxAncestorDiff(self, root):
        if root == None: return -1
        path = []
        res = [-1]
        path.append(root.val)
        self.diff_helper(root, path, res)
        return res[0]

    def constructMaximumBinaryTree(self, nums):
        n = len(nums)
        if n <= 0: return None
        if n == 1: return TreeNode(nums[0])
        max_i = 0; max_v = nums[0]
        for i in range(1, n):
            if nums[i] > max_v:
                max_i = i; max_v = nums[i]
        root = TreeNode(max_v)
        root.left = self.constructMaximumBinaryTree(nums[0:max_i])
        root.right = self.constructMaximumBinaryTree(nums[max_i+1:])
        return root

    def insertIntoMaxTree(self, root, val):
        new_node = TreeNode(val)
        if root == None: return new_node
        if root.val < val:
            new_node.left = root
            return new_node
        root.right = self.insertIntoMaxTree(root.right, val)
        return root

    def widthOfBinaryTree(self, root):
        if root == None: return 0
        queue = [[root, 1]]
        max_len = 0
        while len(queue) > 0:
            qlen = len(queue)
            left = None
            for i in range(qlen):
                cur, i = queue[0]; queue.pop(0)
                if i == 0: left = i
                if i == qlen-1: right = i
                if cur.left: queue.append(cur.left, 2*i)
                if cur.right: queue.append(cur.right, 2*i+1)
            max_len = max(max_len, right-left+1)
        return max_len


    def pruneTree(self, root):
        if root == None: return root
        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        if left == None and right == None and root.val == 0:
            return None
        root.left = left
        root.right = right
        return root

    def sumOfDistancesInTree(self, N, edges):
        if N <= 0: return []
        res = [0] * N
        graph = {}
        for s, e in edges:
            if s not in graph:
                graph[s] = []
            if e not in graph:
                graph[e] = []
            graph[s].append(e)
            graph[e].append(s)
        for i in range(N):
            queue = [[i,0]]
            visited = [False] * N
            visited[i] = True
            while len(queue) > 0:
                cur, dist = queue[0]; queue.pop(0)
                res[cur] += dist
                if cur not in graph: continue
                for e in graph[cur]:
                    if not visited[e]:
                        visited[e] = True
                        queue.append([e, dist+1])
        return res

    def get_father(self, root, father):
        if root == None: return
        if root.left:
            father[root.left] = root
            self.get_father(root.left, father)
        if root.right:
            father[root.right] = root
            self.get_father(root.right, father)

    def dist_bfs(self, start, k, res, father):
        queue = [[start, 0]]
        visited = set()
        visited.add(start)
        while len(queue) > 0:
            cur, dist = queue[0]; queue.pop(0)
            if dist == k:
                res.append(cur.val)
                continue
            if cur.left and cur.left not in visited:
                visited.add(cur.left)
                queue.append([cur.left, dist+1])
            if cur.right and cur.right not in visited:
                visited.add(cur.right)
                queue.append([cur.right, dist+1])
            if cur in father and father[cur] not in visited:
                visited.add(father[cur])
                queue.append([father[cur], dist+1])

    def distanceK(self, root, target, K):
        res = []
        if target == None or root == None: return res
        father = {}
        self.get_father(root, father)
        self.bfs(target, K, res, father)
        return res

    def deepest_helper(self, root):
        if root == None: return None, 0
        if not root.left and not root.right: return root, 1
        left, l_depth = self.deepest_helper(root.left)
        right, r_depth = self.deepest_helper(root.right)
        depth = max(l_depth, r_depth) + 1
        print(root.val, l_depth, r_depth)
        if l_depth == r_depth: return root, depth
        if l_depth > r_depth: return left, depth
        if l_depth < r_depth: return right, depth

    def subtreeWithAllDeepest(self, root):
        return self.deepest_helper(root)[0]

    def increasingBST_helper(self, root):
        if root == None: return root, root
        if not root.left and not root.right: return root, root
        l_s = l_e = root
        if root.left:
            l_s, l_e = self.increasingBST(root.left)
            root.left = None
            l_e.right = root
        r_s = r_e = root
        if root.right:
            r_s, r_e = self.increasingBST(root.right)
            root.right = r_s
            r_e.right = None
        return l_s, r_e

    def increasingBST(self, root):
        return self.increasingBST_helper(root)[0]

    def flipEquiv(self, root1, root2):
        if root1 == None and root2 == None: return True
        if root1 == None or root2 == None: return False
        if root1.val != root2.val: return False
        res = False
        if self.flipEquiv(root1.left, root2.left):
            res |= self.flipEquiv(root1.right, root2.right)
        if res: return res
        if self.flipEquiv(root1.left, root2.right):
            res |= self.flipEquiv(root1.right, root2.left)
        if res: return res

    def isCompleteTree(self, root):
        if root == None: return True
        queue = [root]
        while len(queue) > 0:
            qlen = len(queue)
            flag = False
            for i in range(qlen):
                cur = queue[0]; queue.pop(0)
                if cur == None:
                    flag = True
                    continue
                if flag and cur: return False
                if cur.left: queue.append(cur.left)
                else: queue.append(None)
                if cur.right: queue.append(cur.right)
                else: queue.append(None)
            if flag and len(queue) > 0: return False
        return True

    def mctFromLeafValues(self, arr):
        n = len(arr)
        if n <= 0: return 0
        if n == 1: return arr[0]
        if n == 2: return arr[0] * arr[1]
        import sys
        stack = [sys.maxsize]
        res = 0
        for num in arr:
            while stack[-1] <= num:
                cur = stack[-1]; stack.pop(-1)
                res += cur * min(stack[-1], num)
                print(cur, res)
            stack.append(num)
        print(stack)
        while len(stack) > 2:
            cur = stack[-1]; stack.pop(-1)
            res += cur * stack[-1]
            print(cur, res, len(stack))
        return res

    def vertical_helper(self, root, n_map, idx):
        if root == None: return
        if idx not in n_map: n_map[idx] = []
        n_map[idx].append(root.val)
        self.vertical_helper(root.left, n_map, idx-1)
        self.vertical_helper(root.right, n_map, idx+1)

    def verticalTraversal(self, root):
        res = []
        if root == None: return res
        n_map = {}
        queue = [[root, 0]]
        while len(queue) > 0:
            cur, idx = queue[0]; queue.pop(0)
            if idx not in n_map: n_map[idx] = []
            n_map[idx].append(root.val)
            if cur.left: queue.append([cur.left, idx-1])
            if cur.right: queue.append([cur.right, idx+1])
        idxs = sorted(n_map.keys())
        for idx in idxs:
            res.append(n_map[idx])
        return res

    def recover_helper(self, vals, pad):
        root = TreeNode(int(s[0][0]))
        for i in range(len(vals)-1, 0, -1):
            if vals[i][1] == pad + 1:
                break
        if i == 1:
            root.left = self.recover_helper(vals[1:], pad+1)
            root.right = None
        else:
            root.left = self.recover_helper(vals[1:i], pad+1)
            root.right = self.recover_helper(vals[i:], pad+1)
        return root

    def recoverFromPreorder(self, S):
        n = len(S)
        if n <= 0: return None
        vals = []
        cnt = 0; val = 0
        for i in range(n):
            if S[i] != '-':
                val = val * 10 + int(S[i])
            else:
                if S[i-1] != '-':
                    vals.append([val, cnt])
                    cnt = 0
                cnt += 1
        vals.append([val, cnt])

        return self.recover_helper(vals, 0)

    def pathInZigZagTree(self, label):
        res = []
        level = 0
        while label > 0:
            res.insert(0, label)
            label = label // 2
            level += 1
        flag = False
        print(res)
        while level > 0:
            if flag:
                l = pow(2, level-1)
                h = 2 * l - 1
                res[level-1] = l + h - res[level-1]
                print(level-1, l, h, res[level-1])
            level -= 1
            flag = not flag
        return res

    def deepest_leave_helper(self, root):
        if root == None: return 0, 0
        if not root.left and not root.right:
            return root.val, 1
        l_val, l_depth = self.deepest_leave_helper(root.left)
        r_val, r_depth = self.deepest_leave_helper(root.right)
        depth = max(l_depth, r_depth) + 1
        if l_depth == r_depth: return l_val + r_val, depth
        if l_depth < r_depth: return r_val, depth
        if l_depth > r_depth: return l_val, depth

    def deepestLeavesSum(self, root):
        return self.deepest_leave_helper(root)[0]

    def sum_tree(self, root):
        if root == None: return 0
        left = self.sum_tree(root.left)
        right = self.sum_tree(root.right)
        return root.val + left + right

    def product(self, root, total, res):
        if not root.left and not root.right:
            res[0] = max(res[0], (total-root.val)*root.val)
            return root.val
        left = 0
        if root.left: left = self.product(root.left, total, res)
        right = 0
        if root.right: right = self.product(root.right, total, res)
        cur = root.val + left + right
        res[0] = max(res[0], (total-cur)*cur)
        return cur

    def maxProduct(self, root):
        if root == None: return 0
        total = self.sum_tree(root)
        import sys
        res = [sys.maxsize]
        self.product(root, total, res)
        return res[0] % (pow(10, 9) + 7)

    def need(self, root, cnt_map):
        if root == None: return 0
        left = self.need(root.left, cnt_map)
        right = self.need(root.right, cnt_map)
        cur = left + right + 1 - root.val
        cnt_map[root] = cur
        return cur

    def coin_helper(self, root, need_map, res):
        if root == None: return
        left = right = 0
        if root.left: left = need_map[root.left]
        if root.right: right = need_map[root.right]
        res[0] += abs(left) + abs(right)
        self.coin_helper(root.left, need_map, res)
        self.coin_helper(root.right, need_map, res)

    def distributeCoins(self, root):
        cnt_map = {}
        res = [0]
        self.need(root, cnt_map)
        self.coin_helper(root, cnt_map, res)
        return res[0]






s = Solution()

print(s.pathInZigZagTree(26))
'''
print(s.mctFromLeafValues([6, 15, 5, 2]))
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)

print(s.isCompleteTree(root))
res = s.subtreeWithAllDeepest(root)
print(res.val)

N = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
print(s.sumOfDistancesInTree(N, edges))
'''




