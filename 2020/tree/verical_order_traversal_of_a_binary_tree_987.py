# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        from collections import defaultdict
        node_map = defaultdict(dict)
        node_map[0] = {0: [root.val]}
        queue = []
        queue.append([root, 0, 0])
        min_x = 0; max_x = 0
        while len(queue) > 0:
            node, x, y = queue.pop(0)
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            if node.left:
                if y + 1 not in node_map[x-1]:
                    node_map[x-1][y+1]= []
                node_map[x-1][y+1].append(node.left.val)
                queue.append([node.left, x-1, y+1])
            if node.right:
                if y + 1 not in node_map[x+1]:
                    node_map[x+1][y+1]= []
                node_map[x+1][y+1].append(node.right.val)
                queue.append([node.right, x+1, y+1])
        res = []
        print(node_map)
        for x in range(min_x, max_x+1, 1):
            print('ssss', x, node_map[x])
            nodes = node_map[x]
            cur_res = []
            for y in sorted(nodes.keys()):
                cur_res += sorted(nodes[y])
            res.append(cur_res)
        return res

# [3,9,20,null,null,15,7]
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s = Solution()
    res = s.verticalTraversal(root)
    print(res)

